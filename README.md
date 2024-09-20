# Victory Vision

## Description
Victory Vision est une application web qui permet de saisir des informations, de les enregistrer dans un fichier CSV, d'exécuter un script Python de machine learning et d'afficher les résultats de manière graphique. L'application utilise Flask pour le backend, HTML/CSS pour le frontend, et Matplotlib pour les graphiques.

## Fonctionnalités
- Saisie des informations via un formulaire web.
- Enregistrement des données dans un fichier CSV.
- Exécution d'un modèle de machine learning pour prédire les résultats.
- Affichage graphique des résultats.
- Possibilité de refaire les essais.

## Prérequis
- Python 3.x
- pip

## Installation
1. Clonez le dépôt :
    ```bash
    git clone https://github.com/Kwegit/victory-vision.git
    cd victory-vision
    ```

2. Créez un environnement virtuel et activez-le :
    ```bash
    python -m venv venv
    source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`
    ```

3. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

4. Installez `auto-train` :
    ```bash
   pip install autotrain-advanced    
    ```
   ```bash
   export HF_TOKEN=your_hugging_face_write_token
    autotrain app --host 127.0.0.1 --port 8000    
    ```

## Utilisation

4. Consultez les prédictions.

5. Ouvrez l'interface `auto-train` et configurez les réglages nécessaires.

6. Lancez l'entraînement et revenez 
7. Glissez `app.py` et `main.py` dans le dossier créé par `auto-train`.

8. Exécutez les commandes suivantes dans le dossier `auto-train` :
    ```bash
    uvicorn main:app --reload
    ```
    ```bash
   streamlit run app.py
    ```

9. Remplissez le formulaire et soumettez-le pour enregistrer les données et exécuter le modèle de machine learning.


