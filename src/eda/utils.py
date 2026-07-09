import pandas as pd
from pathlib import Path
from config import DATASET_PATH, TABLES_DIR, FIGURES_DIR, EDA_DIR, LOGS_DIR


def create_report_folders():
    for folder in [TABLES_DIR, FIGURES_DIR, EDA_DIR, LOGS_DIR]:
        folder.mkdir(parents=True, exist_ok=True)


def load_dataset():
    return pd.read_csv(DATASET_PATH)


def save_table(df, filename):
    create_report_folders()
    output_path = TABLES_DIR / filename
    df.to_csv(output_path, index=False)
    return output_path


def print_header(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)