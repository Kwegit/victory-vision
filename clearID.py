import pandas as pd

# Lire le fichier CSV
df = pd.read_csv('le_vrai_merge.csv')

# Colonnes à supprimer
columns_to_drop = [
    'resultId', 'raceId', 'circuitId', 'date', 'driverId', 'constructorId',
    'position', 'time', 'milliseconds', 'fastestLap', 'rank',
    'fastestLapTime', 'statusId', 'Pressure', 'TrackTemp', 'WindDirection', 'fastestLapSpeed', 'points', 'round'
]

# Supprimer les colonnes
df.drop(columns=columns_to_drop, inplace=True)

# Arrondir les colonnes spécifiées à 2 chiffres après la virgule
columns_to_round = ['AirTemp', 'Humidity', 'Rainfall', 'WindSpeed']
df[columns_to_round] = df[columns_to_round].round(2)

# Sauvegarder le fichier CSV modifié
df.to_csv('le_vrai_merge_cleaned.csv', index=False)