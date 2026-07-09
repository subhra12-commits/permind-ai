import pandas as pd

from utils import load_dataset, save_table, print_header, create_report_folders

create_report_folders()
df = load_dataset()

original_columns = df.shape[1]

print_header("STATISTICAL ANALYSIS")

df["question_word_count"] = df["question"].fillna("").astype(str).apply(lambda x: len(x.split()))
df["answer_word_count"] = df["answer"].fillna("").astype(str).apply(lambda x: len(x.split()))

distributions = {
    "source_distribution.csv": df["source"].value_counts().reset_index(),
    "dataset_distribution.csv": df["dataset_name"].value_counts().reset_index(),
    "category_distribution.csv": df["category"].value_counts().reset_index(),
    "difficulty_distribution.csv": df["difficulty"].value_counts().reset_index(),
    "interview_type_distribution.csv": df["interview_type"].value_counts().reset_index(),
    "language_distribution.csv": df["language"].value_counts().reset_index(),
}

for filename, table in distributions.items():
    table.columns = ["Value", "Count"]
    save_table(table, filename)
    print(f"Saved: reports/tables/{filename}")

summary = pd.DataFrame({
    "Metric": [
        "Total Rows",
        "Total Columns",
        "Unique Questions",
        "Unique Categories",
        "Unique Sources",
        "Unique Datasets",
        "Unique Interview Types",
        "Average Question Word Count",
        "Median Question Word Count",
        "Max Question Word Count",
        "Average Answer Word Count",
        "Median Answer Word Count",
        "Max Answer Word Count",
    ],
    "Value": [
        df.shape[0],
        original_columns,
        df["question"].nunique(),
        df["category"].nunique(),
        df["source"].nunique(),
        df["dataset_name"].nunique(),
        df["interview_type"].nunique(),
        round(df["question_word_count"].mean(), 2),
        df["question_word_count"].median(),
        df["question_word_count"].max(),
        round(df["answer_word_count"].mean(), 2),
        df["answer_word_count"].median(),
        df["answer_word_count"].max(),
    ]
})

save_table(summary, "statistics_summary.csv")

print("\nStatistics Summary:")
print(summary)

print("\nStatistical analysis completed successfully.")