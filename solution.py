import pandas as pd
import os

def generate_csv_files(path):
    data = {"phrase": [], "sentiment": []}
    
    for root, _, files in os.walk(path):
        print(f"Procesando la carpeta {root}")
        for file in files:
            print(f"Procesando el archivo {file}")
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    data["phrase"].append(f.read().strip())
                    data["sentiment"].append(os.path.basename(root))

    # Crear el DataFrame y exportarlo a CSV
    df = pd.DataFrame(data)
    output_csv = os.path.join(f"{os.path.basename(path)}_dataset.csv")
    df.to_csv(output_csv, index=False, encoding="utf-8")

# Lista de carpetas a procesar
folders = ["train", "test"]

# Generar archivos CSV para cada carpeta
for folder in folders:
    print(f"Generando archivos CSV para la carpeta {folder}")
    generate_csv_files(folder)