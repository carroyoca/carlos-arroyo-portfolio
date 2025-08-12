import pandas as pd

# Cargar el archivo MERGED_MTFS_WITH ATTACHMENTS
merged_attachments_df = pd.read_excel(r"C:\Users\CARROYO\OBS and the Olympic Channel\Logistics - Logistics Docs\BUSINESS INTELLIGENCE LOGISTICS\OLYMPIC GAMES PARIS 2024\DATABASES\MASTER DATABASE FOR MTFS AND EQUIPMENTS\Control\MERGED_MTFS_WITH ATTACHMENTS.xlsx")

# Cargar el archivo Merged_PARIS_MTFS_DATA
merged_paris_mtfs_df = pd.read_excel(r"C:\Users\CARROYO\OBS and the Olympic Channel\Logistics - Logistics Docs\BUSINESS INTELLIGENCE LOGISTICS\OLYMPIC GAMES PARIS 2024\DATABASES\MASTER DATABASE FOR MTFS AND EQUIPMENTS\Merged_MTFS\Merged_PARIS_MTFS_DATA.xlsx")

# Crear una lista con los valores únicos de la columna "MTF" en merged_paris_mtfs_df
mtf_values = merged_paris_mtfs_df['MTF'].unique()

# Crear la nueva columna "MTF REGISTRADO"
merged_attachments_df['MTF REGISTRADO'] = merged_attachments_df['H'].apply(lambda x: 'si' if x in mtf_values else 'no')

# Guardar el archivo actualizado
output_path = r"C:\Users\CARROYO\OBS and the Olympic Channel\Logistics - Logistics Docs\BUSINESS INTELLIGENCE LOGISTICS\OLYMPIC GAMES PARIS 2024\DATABASES\MASTER DATABASE FOR MTFS AND EQUIPMENTS\Control\MERGED_MTFS_WITH ATTACHMENTS.xlsx"
merged_attachments_df.to_excel(output_path, index=False)

print("Archivo actualizado y guardado exitosamente en:", output_path)
