import pandas as pd
from pathlib import Path

INPUT_FILE = "datasets/merged/master_interview_dataset.csv"
OUTPUT_FILE = "datasets/final/final_interview_dataset.csv"

Path("datasets/final").mkdir(parents=True, exist_ok=True)

df = pd.read_csv(INPUT_FILE)

print("=" * 70)
print("MASTER DATASET CLEANING")
print("=" * 70)

before_rows = len(df)

# Normalize text before duplicate removal

df["question"] = df["question"].fillna("").astype(str).str.strip()
df["answer"] = df["answer"].fillna("").astype(str).str.strip()
df["category"] = df["category"].fillna("General").astype(str).str.strip()
df["subcategory"] = df["subcategory"].fillna("General").astype(str).str.strip()
df["difficulty"] = df["difficulty"].fillna("Unknown").astype(str).str.strip()

df = df[df["question"] != ""]
df = df[df["question"].str.lower() != "nan"]

df["difficulty"] = (
    df["difficulty"]
    .str.lower()
    .replace({
        "easy": "Easy",
        "medium": "Medium",
        "hard": "Hard",
        "unknown": "Unknown"
    })
)

df["category"] = df["category"].replace("", "General")
df["subcategory"] = df["subcategory"].replace("", "General")

before_duplicates = len(df)

df = df.drop_duplicates(
    subset=["question", "answer"],
    keep="first"
)

duplicates_removed = before_duplicates - len(df)

df.reset_index(drop=True, inplace=True)
df["id"] = range(1, len(df) + 1)

df.to_csv(OUTPUT_FILE, index=False)

print(f"Rows before cleaning       : {before_rows}")
print(f"Duplicate questions removed: {duplicates_removed}")
print(f"Final rows                 : {len(df)}")
print(f"Saved to                   : {OUTPUT_FILE}")