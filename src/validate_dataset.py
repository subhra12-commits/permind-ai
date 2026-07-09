import pandas as pd
from pathlib import Path

INPUT_FILE = "datasets/final/final_interview_dataset.csv"

REPORT_DIR = Path("reports/tables")
REPORT_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(INPUT_FILE)

print("=" * 70)
print("MASTER DATASET VALIDATION REPORT")
print("=" * 70)

print(f"\nDataset Shape: {df.shape}")

print("\nColumns:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nEmpty Questions:")
empty_questions = df["question"].astype(str).str.strip().eq("").sum()
print(empty_questions)

print("\nEmpty Answers:")
empty_answers = df["answer"].astype(str).str.strip().eq("").sum()
print(empty_answers)

print("\nDuplicate Full Rows:")
print(df.duplicated().sum())

print("\nDuplicate Questions:")
print(df["question"].duplicated().sum())

print("\nSource Distribution:")
source_dist = df["source"].value_counts()
print(source_dist)

print("\nDataset Name Distribution:")
dataset_dist = df["dataset_name"].value_counts()
print(dataset_dist)

print("\nInterview Type Distribution:")
interview_type_dist = df["interview_type"].value_counts()
print(interview_type_dist)

print("\nCategory Distribution:")
category_dist = df["category"].value_counts()
print(category_dist.head(20))

print("\nDifficulty Distribution:")
difficulty_dist = df["difficulty"].value_counts()
print(difficulty_dist)

source_dist.to_csv(REPORT_DIR / "source_distribution.csv")
dataset_dist.to_csv(REPORT_DIR / "dataset_distribution.csv")
interview_type_dist.to_csv(REPORT_DIR / "interview_type_distribution.csv")
category_dist.to_csv(REPORT_DIR / "category_distribution.csv")
difficulty_dist.to_csv(REPORT_DIR / "difficulty_distribution.csv")

print("\nValidation tables saved to reports/tables/")