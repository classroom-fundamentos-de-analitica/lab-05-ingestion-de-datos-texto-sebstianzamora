import pandas as pd
import os

def generar_csv_test_train(path):
    data = {"phrase": [], "sentiment": []}
    
    for root, _, files in os.walk(path):
        print(f"Recorriendo la carpeta {root}")
        for file in files:
            print(f"Recorriendo el archivo {file}")
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    data["phrase"].append(f.read().strip())
                    data["sentiment"].append(os.path.basename(root))

    df = pd.DataFrame(data)
    output_csv = os.path.join(f"{os.path.basename(path)}_dataset.csv")
    df.to_csv(output_csv, index=False, encoding="utf-8")

# carpetas
folders = ["train", "test"]

for folder in folders:
    print(f"Generando archivos CSV para la carpeta {folder}")
    generar_csv_test_train(folder)

# test_dataset = pd.read_csv("test_dataset.csv")
# counts = test_dataset["sentiment"].value_counts()
# print(counts["neutral"])
# print(counts["positive"])
# print(counts["negative"])


# train_dataset = pd.read_csv("train_dataset.csv")
# print(train_dataset.columns[0]) 
# print(train_dataset.columns[1])

# counts = train_dataset["sentiment"].value_counts()

# print(counts["neutral"])
# print(counts["positive"])
# print(counts["negative"])