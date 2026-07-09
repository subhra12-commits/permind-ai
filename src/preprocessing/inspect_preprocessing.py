import pandas as pd

from config import OUTPUT_DATASET

df = pd.read_csv(OUTPUT_DATASET)

print("=" * 70)
print("PREPROCESSING INSPECTION")
print("=" * 70)

columns = [
    "question",
    "processed_question",
    "answer",
    "processed_answer"
]

print(df[columns].head(10))

print("\nDataset Shape:")
print(df.shape)

print("\nNull Values:")
print(df[columns].isnull().sum())