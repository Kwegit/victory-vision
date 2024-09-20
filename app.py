import streamlit as st
import pandas as pd
import requests

# Lire le fichier CSV fourni
df = pd.read_csv('le_vrai_merge_cleaned.csv')

st.title('Prédictions F1 - Sélectionnez plusieurs pilotes')

# Extraire les données uniques des courses
courses = df['races_name'].unique()

# Formulaire pour sélectionner une course
selected_course = st.selectbox('Sélectionner une course', courses)

# Filtrer les pilotes qui ont participé à la course sélectionnée
filtered_df = df[df['races_name'] == selected_course]
pilotes = (filtered_df['forename'] + ' ' + filtered_df['surname']).unique()

# Sélection des pilotes
selected_pilots = st.multiselect('Sélectionner les pilotes', pilotes)

# Créer des dictionnaires pour stocker les écuries et les positions sur la grille de chaque pilote
constructor_dict = {}
grid_dict = {}

# Ajouter une sélection d'écurie et de position sur la grille pour chaque pilote sélectionné
for pilot in selected_pilots:
    # Filtrer les écuries correspondant au pilote pour la course sélectionnée
    pilot_df = filtered_df[(filtered_df['forename'] + ' ' + filtered_df['surname']) == pilot]
    constructors = pilot_df['constructor_name'].unique()

    selected_constructor = st.selectbox(f"Sélectionner l'écurie pour {pilot}", constructors)
    constructor_dict[pilot] = selected_constructor

    grid_position = st.number_input(f'Position sur la grille pour {pilot}', min_value=1, max_value=20)
    grid_dict[pilot] = grid_position

# Autres informations globales (valables pour tous les pilotes)
laps = st.number_input('Nombre de tours')
AirTemp = st.number_input('Température de l\'air (°C)')
Humidity = st.number_input('Humidité (%)', min_value=0.0, max_value=100.0)
Rainfall = st.number_input('Précipitations (mm)')
WindSpeed = st.number_input('Vitesse du vent (km/h)')

submit = st.button('Lancer les prédictions')

# Lorsque l'utilisateur soumet le formulaire
if submit:
    # Préparer les données pour chaque pilote sélectionné
    input_data = []
    for pilot in selected_pilots:
        # Séparer le prénom et le nom
        forename, surname = pilot.split(' ')

        # Chercher les données du pilote pour la course sélectionnée
        pilot_data = filtered_df[(filtered_df['forename'] == forename) & (filtered_df['surname'] == surname)]

        if not pilot_data.empty:
            input_data.append({
                "ID": int(pilot_data.iloc[0]['ID']),
                "year": int(pilot_data.iloc[0]['year']),
                "races_name": selected_course,
                "forename": forename,
                "surname": surname,
                "constructor_name": constructor_dict[pilot],  # Utiliser l'écurie sélectionnée pour ce pilote
                "number": int(pilot_data.iloc[0]['number']),
                "grid": grid_dict[pilot],  # Utiliser la position de grille pour ce pilote
                "target": 0,  # Peut-être calculé ou laissé par défaut
                "laps": laps,
                "status": "active",  # Peut-être modifié selon les données
                "AirTemp": AirTemp,
                "Humidity": Humidity,
                "Rainfall": Rainfall,
                "WindSpeed": WindSpeed
            })

    # Envoyer les données au backend FastAPI pour les prédictions
    url = 'http://localhost:8000/predict'
    response = requests.post(url, json=input_data)

    # Afficher les résultats sous forme de classement
    if response.status_code == 200:
        predictions = response.json()["predictions"]

        # Créer une liste pour stocker les résultats
        classement = []
        for i, prediction in enumerate(predictions):
            # Utiliser les données des pilotes sélectionnés pour afficher les prénoms
            pilot_name = selected_pilots[i]  # Utiliser l'ordre de sélection des pilotes
            classement.append({
                "Prénom": pilot_name.split(' ')[0],  # Extraire le prénom
                "Place prédite": prediction['predicted_place'],
                "Probabilité": f"{prediction['probability']:.2f}"  # Afficher avec 2 décimales
            })

        # Convertir la liste de résultats en DataFrame et trier par place prédite
        classement_df = pd.DataFrame(classement)
        classement_df = classement_df.sort_values(by='Place prédite')

        # Afficher le classement sous forme de tableau visuel
        st.subheader(f"Classement prédictif pour la course {selected_course}")
        st.table(classement_df)  # Utiliser st.table pour afficher un tableau propre
    else:
        st.error("Une erreur s'est produite lors de la prédiction.")
