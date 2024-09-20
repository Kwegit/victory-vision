import pandas as pd

def replace_svg_with_png(input_file, output_file):
    df = pd.read_csv(input_file)

    df['circuit_image'] = df['circuit_image'].str.replace('.svg', '.png')

    df.to_csv(output_file, index=False)

    print(f"Traitement terminé. Fichier de sortie créé à '{output_file}'.")

input_file = '../Datas/le_merge_image.csv'
output_file = ('../Datas/le_merge_image_repaired.csv')

replace_svg_with_png(input_file, output_file)
