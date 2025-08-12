import os
import pandas as pd

# Ruta de la carpeta que contiene los archivos
folder_path = r'C:\Users\CARROYO\OBS and the Olympic Channel\Logistics - Logistics Docs\INVENTORY\Stock For analysis of equipments not moved'

# Ruta de salida para el archivo resultante
output_path = r'C:\Users\CARROYO\OneDrive - OBS and the Olympic Channel\Desktop\Analisis stock\equipos_no_movidos.csv'

# Lista de ubicaciones de "SUMMER WH"
summer_wh_locations = [
    "Summer WH OBS Department",
    "Summer WH CLARIFICATION ZONE",
    "Summer WH BENG OPEN AREA",
    "Summer WH LOG FLOOR WAREHOUSE",
    "Summer WH COMM",
    "Summer WH LOG RACKING ZONE",
    "Summer WH VENDORS",
    "Summer WH FLD",
    "Summer WH FLD OPEN AREA",
    "Summer WH OFFICES",
    "Summer WH COMM SW TEAMS",
    "Summer WH TO BE DESTROYED",
    "Summer WH COMM VENUES SW",
    "Summer WH TECH AREAS"
]

# Obtener todos los archivos Excel en la carpeta
excel_files = [f for f in os.listdir(folder_path) if f.endswith('.xlsx')]

# Crear una lista para almacenar los DataFrames
df_list = []

# Leer todos los archivos y guardarlos en la lista
for file in excel_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_excel(file_path)
    
    # Convertir todas las columnas a minúsculas para evitar problemas de capitalización
    df.columns = df.columns.str.lower()
    
    # Filtrar por equipos no vacíos y ubicaciones de SUMMER WH
    df_filtered = df[df['equipment'].notna() & df['storagetypedesc'].isin(summer_wh_locations)]
    df_list.append(df_filtered[['equipment', 'storagetypedesc']])  # Solo necesitamos estas dos columnas

# Inicializar un DataFrame con los equipos del primer archivo
common_equipment = df_list[0][['equipment']].drop_duplicates()

# Iterar sobre los demás archivos y hacer una intersección para obtener los equipos comunes
for df in df_list[1:]:
    common_equipment = pd.merge(common_equipment, df[['equipment']].drop_duplicates(), on='equipment', how='inner')

# Exportar los resultados a CSV
common_equipment.to_csv(output_path, index=False)

print(f"Análisis completado. Los equipos no movidos han sido guardados en {output_path}")
