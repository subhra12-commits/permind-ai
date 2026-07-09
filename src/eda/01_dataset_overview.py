import pandas as pd

from utils import (
    load_dataset,
    save_table,
    print_header,
    create_report_folders
)

create_report_folders()

df = load_dataset()

print_header("DATASET OVERVIEW")

# ==========================================================
# Basic Information
# ==========================================================

print(f"\nDataset Shape : {df.shape}")

print("\nColumns:")
for col in df.columns:
    print(f"- {col}")

print("\nData Types:")
print(df.dtypes)

print("\nMemory Usage:")
memory_mb = df.memory_usage(deep=True).sum() / 1024**2
print(f"{memory_mb:.2f} MB")

# ==========================================================
# Create Overview Table
# ==========================================================

overview = pd.DataFrame({
    "Column": df.columns,
    "Data Type": df.dtypes.astype(str).values,
    "Missing Values": df.isnull().sum().values,
    "Unique Values": [df[col].nunique() for col in df.columns]
})

save_table(
    overview,
    "dataset_overview.csv"
)

# ==========================================================
# Sample Data
# ==========================================================

print("\nFirst 5 Rows:")
print(df.head())

print("\nLast 5 Rows:")
print(df.tail())

print("\nDataset overview saved to:")
print("reports/tables/dataset_overview.csv")