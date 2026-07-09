import pandas as pd

DATASETS = [
    "datasets/raw/huggingface/ai_interview_questions_train.csv",
    "datasets/raw/huggingface/programming_interview_train.csv",
    "datasets/raw/huggingface/software_engineering_hf_train.csv",
    "datasets/raw/kaggle/hr_technical_interview/full_interview_questions_dataset.csv",
    "datasets/raw/kaggle/resume_job_description/resume_dataset_1200.csv",
    "datasets/raw/kaggle/software_engineering_kaggle/Software Questions.csv"
]

ENCODINGS = ["utf-8", "cp1252", "latin1"]

for file in DATASETS:
    print("\n" + "=" * 80)
    print(file)

    df = None

    for encoding in ENCODINGS:
        try:
            df = pd.read_csv(file, encoding=encoding)
            print(f"\nEncoding Used: {encoding}")
            break
        except Exception:
            continue

    if df is None:
        print("Unable to read dataset.")
        continue

    print(f"Shape: {df.shape}")

    print("\nColumns:")
    for column in df.columns:
        print("-", column)

    print("\nFirst 2 Rows:")
    print(df.head(2))