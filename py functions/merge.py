import pandas as pd
import requests
from bs4 import BeautifulSoup

def extract_image_url(page_url):
    response = requests.get(page_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        image_tag = soup.find('img')  # Adjust the selector based on the website's structure
        if image_tag and 'src' in image_tag.attrs:
            return image_tag['src']
    return page_url  # Return the original URL if no image is found

def update_image_links(input_file, output_file):
    # Lire le fichier CSV
    df = pd.read_csv(input_file)

    # Extraire les liens d'image des URLs dans la colonne circuit_image
    df['circuit_image'] = df['circuit_image'].apply(extract_image_url)

    # Écrire le DataFrame mis à jour dans un nouveau fichier CSV
    df.to_csv(output_file, index=False)

    print(f"Traitement terminé. Fichier de sortie créé à '{output_file}'.")

input_file = '../Datas/le_merge_image_repaired.csv'
output_file = '../Datas/le_merge_image_repaired_final.csv'
update_image_links(input_file, output_file)z