import zipfile
import subprocess
import pandas as pd
from datasets import load_dataset
from pathlib import Path
from datetime import datetime

from dataset_registry import HUGGINGFACE_DATASETS, KAGGLE_DATASETS

BASE_DIR = Path("datasets")
RAW_DIR = BASE_DIR / "raw"
HF_DIR = RAW_DIR / "huggingface"
KAGGLE_DIR = RAW_DIR / "kaggle"
METADATA_FILE = BASE_DIR / "dataset_metadata.csv"


def create_folders():
    for folder in [
        HF_DIR,
        KAGGLE_DIR,
        BASE_DIR / "processed",
        BASE_DIR / "merged",
        BASE_DIR / "final",
    ]:
        folder.mkdir(parents=True, exist_ok=True)


def save_metadata(dataset_name, source, rows, columns, status):
    new_row = pd.DataFrame([{
        "dataset_name": dataset_name,
        "source": source,
        "rows": rows,
        "columns": columns,
        "status": status,
        "download_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }])

    if METADATA_FILE.exists():
        old = pd.read_csv(METADATA_FILE)
        final = pd.concat([old, new_row], ignore_index=True)
    else:
        final = new_row

    final.to_csv(METADATA_FILE, index=False)


def download_huggingface_dataset(dataset_name, output_name):
    try:
        print(f"\nDownloading HF: {dataset_name}")
        dataset = load_dataset(dataset_name)

        for split_name, split_data in dataset.items():
            df = split_data.to_pandas()
            output_path = HF_DIR / f"{output_name}_{split_name}.csv"
            df.to_csv(output_path, index=False)

            save_metadata(output_name, f"Hugging Face: {dataset_name}", df.shape[0], df.shape[1], "Downloaded")
            print(f"Saved: {output_path}")

    except Exception as e:
        print(f"Failed HF dataset {dataset_name}: {e}")
        save_metadata(output_name, f"Hugging Face: {dataset_name}", 0, 0, f"Failed: {e}")


def download_kaggle_dataset(dataset_name, output_name):
    try:
        print(f"\nDownloading Kaggle: {dataset_name}")
        output_folder = KAGGLE_DIR / output_name
        output_folder.mkdir(parents=True, exist_ok=True)

        subprocess.run(
            ["kaggle", "datasets", "download", "-d", dataset_name, "-p", str(output_folder)],
            check=True
        )

        for zip_file in output_folder.glob("*.zip"):
            with zipfile.ZipFile(zip_file, "r") as zip_ref:
                zip_ref.extractall(output_folder)
            zip_file.unlink()

        csv_files = list(output_folder.glob("*.csv"))
        total_rows = 0
        total_columns = 0

        for csv_file in csv_files:
            try:
                df = pd.read_csv(csv_file)
                total_rows += df.shape[0]
                total_columns = max(total_columns, df.shape[1])
            except Exception:
                pass

        save_metadata(output_name, f"Kaggle: {dataset_name}", total_rows, total_columns, "Downloaded")
        print(f"Saved in: {output_folder}")

    except Exception as e:
        print(f"Failed Kaggle dataset {dataset_name}: {e}")
        save_metadata(output_name, f"Kaggle: {dataset_name}", 0, 0, f"Failed: {e}")


def main():
    create_folders()

    for dataset in HUGGINGFACE_DATASETS:
        download_huggingface_dataset(dataset["name"], dataset["output"])

    for dataset in KAGGLE_DATASETS:
        download_kaggle_dataset(dataset["name"], dataset["output"])

    print("\nAll dataset download attempts completed.")
    print(f"Metadata saved to: {METADATA_FILE}")


if __name__ == "__main__":
    main()