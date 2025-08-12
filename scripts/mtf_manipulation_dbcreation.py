import pandas as pd

# Cargar el archivo completo para verificar las columnas
full_dataset_df = pd.read_excel(r"C:\Users\CARROYO\OBS and the Olympic Channel\Logistics - Logistics Docs\BUSINESS INTELLIGENCE LOGISTICS\OLYMPIC GAMES PARIS 2024\DATABASES\MASTER DATABASE FOR MTFS AND EQUIPMENTS\Control\full_dataset_with_row_ids.xlsx")

# Imprimir los nombres de las columnas del archivo full_dataset_df
print("Columnas en full_dataset_with_row_ids:", full_dataset_df.columns)

# Aquí puedes revisar manualmente el nombre de la columna que quieres usar en lugar de 'B'
# Sustituye 'NombreCorrectoDeLaColumna' por el nombre correcto de la columna

# Ahora, carga el archivo de attachments
attachments_df = pd.read_excel(r"C:\Users\CARROYO\OBS and the Olympic Channel\Logistics - Logistics Docs\BUSINESS INTELLIGENCE LOGISTICS\OLYMPIC GAMES PARIS 2024\DATABASES\MASTER DATABASE FOR MTFS AND EQUIPMENTS\Control\attachments_with_rows_and_parent.xlsx")

# Realizar el cruce usando el nombre correcto de la columna
merged_df = pd.merge(attachments_df, full_dataset_df[['Row ID (Parent ID)', 'MTF Number']], how='left', left_on='Parent ID', right_on='Row ID (Parent ID)')

# Añadir el valor de la columna correcta a la columna H del archivo attachments
merged_df['H'] = merged_df['MTF Number']

# Seleccionar solo las columnas necesarias (excluyendo la columna que fue añadida durante el merge)
final_df = merged_df.drop(columns=['Row ID (Parent ID)', 'MTF Number'])

# Guardar el archivo resultante
output_path = r"C:\Users\CARROYO\OBS and the Olympic Channel\Logistics - Logistics Docs\BUSINESS INTELLIGENCE LOGISTICS\OLYMPIC GAMES PARIS 2024\DATABASES\MASTER DATABASE FOR MTFS AND EQUIPMENTS\Control\MERGED_MTFS_WITH ATTACHMENTS.xlsx"
final_df.to_excel(output_path, index=False)

print("Archivo guardado exitosamente en:", output_path)
