from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np

# Charger le modèle pré-entrainé
model = joblib.load('autotrain-ibmjr-cqffg/model.joblib')

# Initialiser FastAPI
app = FastAPI()


# Définir le schéma des données d'entrée (validation des champs)
class TestData(BaseModel):
    ID: int
    year: int
    races_name: str
    forename: str
    surname: str
    constructor_name: str
    number: int
    grid: int
    target: int
    laps: int
    status: str
    AirTemp: float
    Humidity: float
    Rainfall: float
    WindSpeed: float


# Endpoint de prédiction
@app.post("/predict")
async def predict(test_data: list[TestData]):
    # Convertir les données en DataFrame
    data = pd.DataFrame([item.dict() for item in test_data])

    # Assurer la conversion des types NumPy en types Python natifs
    data = data.applymap(lambda x: x.item() if isinstance(x, (np.generic, np.ndarray)) else x)

    # Utiliser predict_proba pour obtenir les probabilités des classes
    predictions_proba = model.predict_proba(data)

    # Initialiser un tableau pour stocker les places
    assigned_places = np.zeros(len(data), dtype=int)

    # Pour suivre les places déjà assignées
    used_places = set()

    # Trier les probabilités et attribuer les places
    for i in range(len(data)):
        sorted_indices = np.argsort(-predictions_proba[i])
        for idx in sorted_indices:
            place = idx + 1
            if place not in used_places:
                assigned_places[i] = place
                used_places.add(place)
                break

    # Préparer les résultats
    results = [
        {
            "ID": int(data.loc[i, "ID"]),  # Assurer que ID est un int natif
            "sample": i,
            "predicted_place": int(assigned_places[i]),  # Conversion en int natif
            "probability": round(float(predictions_proba[i, assigned_places[i] - 1]), 2)  # Conversion en float natif
        }
        for i in range(len(data))
    ]

    return {"predictions": results}
