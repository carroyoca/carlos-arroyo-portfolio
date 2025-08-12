import pandas as pd
import os

# Lista de archivos CSV
archivos_csv = [
    r"C:\Users\carroyo\Downloads\ingest_manualmatches_7digital - Hoja 1.csv",
    r"C:\Users\carroyo\Downloads\ingest_manualmatches_qobuz - Hoja 1.csv",
    r"C:\Users\carroyo\Downloads\ingest_manualmatches_itunes - Hoja 1.csv",
    r"C:\Users\carroyo\Downloads\ingest_manualmatches_facebook - Hoja 1.csv",
    r"C:\Users\carroyo\Downloads\ingest_manualmatches_deezer - Hoja 1.csv",
    r"C:\Users\carroyo\Downloads\ingest_manualmatches_amazon - Hoja 1.csv"
]

# Directorio donde se guardarán los archivos nuevos
output_dir = r"C:\Users\carroyo\Documents\QA_ingest_manual_matches"

# Crear directorio si no existe
os.makedirs(output_dir, exist_ok=True)

for archivo in archivos_csv:
    # Leer CSV
    df = pd.read_csv(archivo)

    # Renombrar la sexta columna a "qa_owner"
    df.rename(columns={df.columns[5]: "qa_owner"}, inplace=True)

    # Reemplazar contenido de "qa_owner" por "sgae"
    df["qa_owner"] = "sgae"

    # Guardar archivo modificado
    nuevo_nombre = os.path.basename(archivo).replace('.csv', '_modificado.csv')
    ruta_guardado = os.path.join(output_dir, nuevo_nombre)
    df.to_csv(ruta_guardado, index=False)

print("¡Archivos procesados correctamente!")
