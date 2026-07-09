import pandas as pd
import re
from pathlib import Path
from datetime import datetime

from schema import MASTER_COLUMNS

OUTPUT_DIR = Path("datasets/processed")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def extract_instruction_format(text: str):
    pattern = r"<s>\[INST\](.*?)\[/INST\](.*?)(?:</s>)?$"
    match = re.search(pattern, str(text), re.DOTALL)

    if match:
        question = match.group(1).strip()
        answer = match.group(2).strip()
        return question, answer

    return None, None


def create_master_df(
    df,
    question_col,
    answer_col=None,
    category="Technical",
    subcategory="General",
    difficulty="Unknown",
    source="Hugging Face",
    dataset_name="Unknown",
    interview_type="Technical",
    language="English",
    tags=""
):
    final_df = pd.DataFrame()

    final_df["question"] = df[question_col].astype(str).str.strip()

    if answer_col and answer_col in df.columns:
        final_df["answer"] = df[answer_col].astype(str).str.strip()
    else:
        final_df["answer"] = ""

    final_df["category"] = category
    final_df["subcategory"] = subcategory
    final_df["difficulty"] = difficulty
    final_df["source"] = source
    final_df["dataset_name"] = dataset_name
    final_df["interview_type"] = interview_type
    final_df["language"] = language
    final_df["tags"] = tags
    final_df["created_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    final_df.insert(0, "id", range(1, len(final_df) + 1))

    return final_df[MASTER_COLUMNS]


def standardize_ai_interview_questions():
    input_files = [
        "datasets/raw/huggingface/ai_interview_questions_train.csv",
        "datasets/raw/huggingface/ai_interview_questions_eval.csv"
    ]

    all_rows = []

    for file in input_files:
        df = pd.read_csv(file)
        df.columns = df.columns.str.strip()

        extracted = df["text"].apply(
            lambda x: pd.Series(extract_instruction_format(x))
        )

        extracted.columns = ["question", "answer"]

        extracted["category"] = "Technical"
        extracted["subcategory"] = "General"
        extracted["difficulty"] = "Unknown"
        extracted["source"] = "Hugging Face"
        extracted["dataset_name"] = "AI Interview Questions"
        extracted["interview_type"] = "Technical"
        extracted["language"] = "English"
        extracted["tags"] = "technical, interview, qna"
        extracted["created_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        extracted.insert(0, "id", range(1, len(extracted) + 1))

        all_rows.append(extracted[MASTER_COLUMNS])

    final_df = pd.concat(all_rows, ignore_index=True)
    final_df["id"] = range(1, len(final_df) + 1)

    output_file = OUTPUT_DIR / "hf_ai_interview_questions_standardized.csv"
    final_df.to_csv(output_file, index=False)

    print(f"Saved: {output_file} | Shape: {final_df.shape}")


def standardize_programming_interview():
    file = "datasets/raw/huggingface/programming_interview_train.csv"

    df = pd.read_csv(file)

    # Remove unwanted spaces from column names
    df.columns = df.columns.str.strip()

    final_df = pd.DataFrame()
    final_df["question"] = (
    "[" + df["language"].astype(str).str.strip() + " - " +
    df["level"].astype(str).str.strip() + "] " +
    df["Questions"].astype(str).str.strip()
)
    final_df["answer"] = df["Answers"].astype(str).str.strip()
    final_df["category"] = "Software Engineering"
    final_df["subcategory"] = "Programming"
    final_df["difficulty"] = df["level"].astype(str).str.strip()
    final_df["source"] = "Hugging Face"
    final_df["dataset_name"] = "Programming Interview Questions"
    final_df["interview_type"] = "Coding"
    final_df["language"] = "English"
    final_df["tags"] = "programming, coding, interview"
    final_df["created_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    final_df.insert(0, "id", range(1, len(final_df) + 1))

    final_df = final_df[MASTER_COLUMNS]

    output_file = OUTPUT_DIR / "hf_programming_interview_standardized.csv"
    final_df.to_csv(output_file, index=False)

    print(f"Saved: {output_file} | Shape: {final_df.shape}")


def standardize_software_engineering_hf():
    file = "datasets/raw/huggingface/software_engineering_hf_train.csv"
    df = pd.read_csv(file)
    df.columns = df.columns.str.strip()

    final_df = pd.DataFrame()
    final_df["question"] = df["response"].astype(str).str.strip()
    final_df["answer"] = ""
    final_df["category"] = "Software Engineering"
    final_df["subcategory"] = "Software Engineering"
    final_df["difficulty"] = "Unknown"
    final_df["source"] = "Hugging Face"
    final_df["dataset_name"] = "Software Engineering Interviews HF"
    final_df["interview_type"] = "Technical"
    final_df["language"] = "English"
    final_df["tags"] = df["input"].astype(str).str.strip()
    final_df["created_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    final_df.insert(0, "id", range(1, len(final_df) + 1))

    final_df = final_df[MASTER_COLUMNS]

    output_file = OUTPUT_DIR / "hf_software_engineering_standardized.csv"
    final_df.to_csv(output_file, index=False)

    print(f"Saved: {output_file} | Shape: {final_df.shape}")


def main():
    standardize_ai_interview_questions()
    standardize_programming_interview()
    standardize_software_engineering_hf()

    print("\nHugging Face standardization completed successfully.")


if __name__ == "__main__":
    main()