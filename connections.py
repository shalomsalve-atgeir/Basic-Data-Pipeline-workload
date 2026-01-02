import pandas as pd
import kagglehub
import shutil, os

DATASET = "raghavendragandhi/retail-customer-and-transaction-dataset"
TARGET_DIR = "data"

try:
    dataset_path = kagglehub.dataset_download(DATASET)
    print("Dataset downloaded at:", dataset_path)
except Exception as e:
    print("Error downloading dataset:", e)
    exit(1)

os.makedirs(TARGET_DIR, exist_ok=True)

for file in os.listdir(dataset_path):
    if file.endswith(".csv"):
        shutil.copy(
            os.path.join(dataset_path, file),
            os.path.join(TARGET_DIR, file)
        )

print("CSV files copied to", TARGET_DIR)


# TABLE COLUMNS AND DATA TYPES CHECKING
for file in os.listdir(r"C:\Users\shalom BSC CS\Documents\DE JOURNEY\PY PROJECTS\Basic_DataPipeline_workload\data"):
    if file.endswith(".csv"):
        print(f"Name of the file: {file}")
        print("\n")
        df = pd.read_csv(os.path.join("data", file))
        print(df.head(5))
        print(df.info())
        print("\n\n")

# MYSQL CONNECTION CHECKING
import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="wellerman",
        database= "basic_DataPipeline"
    )

    if conn.is_connected():
        print(" MySQL connection successful")
    conn.close()

except Exception as e:
    print(" mysql database connection failed")
    print(e)
