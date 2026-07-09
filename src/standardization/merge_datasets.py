import pandas as pd
from pathlib import Path

PROCESSED_DIR = Path("datasets/processed")
MERGED_DIR = Path("datasets/merged")

MERGED_DIR.mkdir(parents=True, exist_ok=True)

MASTER_FILE = MERGED_DIR / "master_interview_dataset.csv"


def merge_all_datasets():

    csv_files = sorted(PROCESSED_DIR.glob("*_standardized.csv"))

    if len(csv_files) == 0:
        print("No standardized datasets found.")
        return

    merged_df = pd.DataFrame()

    print("=" * 70)
    print("MERGING STANDARDIZED DATASETS")
    print("=" * 70)

    for file in csv_files:

        df = pd.read_csv(file)

        print(f"{file.name:<55} {df.shape}")

        merged_df = pd.concat(
            [merged_df, df],
            ignore_index=True
        )

    # Remove duplicate rows
    before = len(merged_df)

    merged_df.drop_duplicates(inplace=True)

    after = len(merged_df)

    duplicates_removed = before - after

    # Reset IDs
    merged_df.reset_index(drop=True, inplace=True)

    merged_df["id"] = range(1, len(merged_df) + 1)

    merged_df.to_csv(MASTER_FILE, index=False)

    print("\n" + "=" * 70)
    print("MERGE SUMMARY")
    print("=" * 70)

    print(f"Datasets merged      : {len(csv_files)}")
    print(f"Rows before cleanup  : {before}")
    print(f"Duplicates removed   : {duplicates_removed}")
    print(f"Final rows           : {after}")

    print(f"\nSaved to:\n{MASTER_FILE}")


if __name__ == "__main__":
    merge_all_datasets()