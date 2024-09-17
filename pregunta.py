import os
import csv
import pandas as pd


def create_test_and_train_dataset():
    paths = ["train", "test"]
    output_files = ["train_dataset.csv", "test_dataset.csv"]
    folders = ["negative", "positive", "neutral"]
    
    for i, output_file in enumerate(output_files):
        with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["phrase", "sentiment"])
        
        for folder in folders:
            folder_path = os.path.join("data", paths[i], folder)
            
            if not os.path.exists(folder_path):
                print(f"La carpeta {folder_path} no existe.")
                continue
            
            with open(output_file, "a", newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                
                for filename in os.listdir(folder_path):
                    if filename.endswith(".txt"):
                        file_path = os.path.join(folder_path, filename)
                        try:
                            with open(file_path, "r", encoding="utf-8") as f:
                                content = f.read().strip()
                                writer.writerow([content, folder])
                        except Exception as e:
                            print(f"Error al leer el archivo {file_path}: {str(e)}")

    print("Proceso completado. Archivos CSV creados.")

if __name__ == "__main__":
    create_test_and_train_dataset()
