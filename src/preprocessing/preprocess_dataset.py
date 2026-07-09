import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))

from config import INPUT_DATASET, OUTPUT_DATASET
from utils import load_dataset, save_dataset
from text_preprocessor import TextPreprocessor


def main():
    print("=" * 70)
    print("PREPROCESSING DATASET")
    print("=" * 70)

    df = load_dataset(INPUT_DATASET)

    preprocessor = TextPreprocessor()

    df["processed_question"] = df["question"].apply(preprocessor.preprocess)
    df["processed_answer"] = df["answer"].apply(preprocessor.preprocess)

    save_dataset(df, OUTPUT_DATASET)

    print(f"Rows processed: {len(df)}")
    print("Preprocessing completed successfully.")


if __name__ == "__main__":
    main()