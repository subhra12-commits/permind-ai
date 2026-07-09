import pandas as pd
from pathlib import Path
from datetime import datetime

from schema import MASTER_COLUMNS

OUTPUT_DIR = Path("datasets/processed")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

DATASET_CONFIGS = [
    {
        "input_file": "datasets/raw/kaggle/hr_technical_interview/full_interview_questions_dataset.csv",
        "output_file": "kaggle_hr_technical_standardized.csv",
        "encoding": "utf-8",
        "question_col": "question",
        "answer_col": None,
        "category_col": "category",
        "subcategory_col": "role",
        "difficulty_col": "difficulty",
        "dataset_name": "HR Technical Interview",
        "interview_type": "HR/Technical",
        "tags": "hr, technical, interview"
    },
    {
        "input_file": "datasets/raw/kaggle/software_engineering_kaggle/Software Questions.csv",
        "output_file": "kaggle_software_engineering_standardized.csv",
        "encoding": "latin1",
        "question_col": "Question",
        "answer_col": "Answer",
        "category_col": "Category",
        "subcategory_col": None,
        "difficulty_col": "Difficulty",
        "dataset_name": "Software Engineering Kaggle",
        "interview_type": "Technical",
        "tags": "software engineering, oop, sdlc"
    },
    {
        "input_file": "datasets/raw/kaggle/resume_job_description/resume_dataset_1200.csv",
        "output_file": "kaggle_resume_job_description_standardized.csv",
        "encoding": "utf-8",
        "question_col": None,
        "answer_col": None,
        "category_col": "Current_Job_Title",
        "subcategory_col": "Field_of_Study",
        "difficulty_col": None,
        "dataset_name": "Resume Job Description",
        "interview_type": "Resume-Based",
        "tags": "resume, job description, skills"
    }
]


def get_column_value(df, col_name, default_value):
    if col_name and col_name in df.columns:
        return df[col_name].astype(str).str.strip()
    return default_value


def standardize_dataset(config):
    print(f"\nProcessing: {config['dataset_name']}")

    df = pd.read_csv(
        config["input_file"],
        encoding=config["encoding"]
    )

    df.columns = df.columns.str.strip()

    final_df = pd.DataFrame()

    if config["question_col"]:
        final_df["question"] = df[config["question_col"]].astype(str).str.strip()
    else:
        final_df["question"] = (
            "Generate interview questions based on this resume and job description: "
            + df["Skills"].astype(str)
            + " | Target Role: "
            + df["Target_Job_Description"].astype(str)
        )

    if config["answer_col"]:
        final_df["answer"] = df[config["answer_col"]].astype(str).str.strip()
    else:
        final_df["answer"] = ""

    final_df["category"] = get_column_value(df, config["category_col"], "General")
    final_df["subcategory"] = get_column_value(df, config["subcategory_col"], "General")
    final_df["difficulty"] = get_column_value(df, config["difficulty_col"], "Unknown")

    final_df["source"] = "Kaggle"
    final_df["dataset_name"] = config["dataset_name"]
    final_df["interview_type"] = config["interview_type"]
    final_df["language"] = "English"
    final_df["tags"] = config["tags"]
    final_df["created_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    final_df.insert(0, "id", range(1, len(final_df) + 1))
    final_df = final_df[MASTER_COLUMNS]

    output_path = OUTPUT_DIR / config["output_file"]
    final_df.to_csv(output_path, index=False)

    print(f"Saved: {output_path} | Shape: {final_df.shape}")


def main():
    for config in DATASET_CONFIGS:
        standardize_dataset(config)

    print("\nKaggle standardization completed successfully.")


if __name__ == "__main__":
    main()