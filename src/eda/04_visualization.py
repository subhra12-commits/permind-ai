import matplotlib.pyplot as plt

from utils import (
    load_dataset,
    print_header,
    create_report_folders,
)
from config import FIGURES_DIR

create_report_folders()

df = load_dataset()

print_header("DATA VISUALIZATION")

# ==========================================================
# Helper Function
# ==========================================================

def save_plot(filename):
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / filename, dpi=300)
    plt.close()
    print(f"Saved: reports/figures/{filename}")


# ==========================================================
# Source Distribution
# ==========================================================

df["source"].value_counts().plot(kind="bar")

plt.title("Source Distribution")
plt.xlabel("Source")
plt.ylabel("Count")

save_plot("source_distribution.png")

# ==========================================================
# Dataset Distribution
# ==========================================================

df["dataset_name"].value_counts().plot(kind="bar")

plt.title("Dataset Distribution")
plt.xlabel("Dataset")
plt.ylabel("Count")
plt.xticks(rotation=25, ha="right")

save_plot("dataset_distribution.png")

# ==========================================================
# Interview Type Distribution
# ==========================================================

df["interview_type"].value_counts().plot(kind="bar")

plt.title("Interview Type Distribution")
plt.xlabel("Interview Type")
plt.ylabel("Count")

save_plot("interview_type_distribution.png")

# ==========================================================
# Difficulty Distribution
# ==========================================================

df["difficulty"].value_counts().plot(kind="bar")

plt.title("Difficulty Distribution")
plt.xlabel("Difficulty")
plt.ylabel("Count")

save_plot("difficulty_distribution.png")

# ==========================================================
# Top 15 Categories
# ==========================================================

(
    df["category"]
    .value_counts()
    .head(15)
    .plot(kind="bar")
)

plt.title("Top 15 Categories")
plt.xlabel("Category")
plt.ylabel("Count")
plt.xticks(rotation=45, ha="right")

save_plot("category_distribution.png")

# ==========================================================
# Question Length Histogram
# ==========================================================

question_lengths = (
    df["question"]
    .fillna("")
    .astype(str)
    .apply(lambda x: len(x.split()))
)

plt.hist(question_lengths, bins=30)

plt.title("Question Length Distribution")
plt.xlabel("Words")
plt.ylabel("Frequency")

save_plot("question_length_histogram.png")

# ==========================================================
# Answer Length Histogram
# ==========================================================

answer_lengths = (
    df["answer"]
    .fillna("")
    .astype(str)
    .apply(lambda x: len(x.split()))
)

plt.hist(answer_lengths, bins=30)

plt.title("Answer Length Distribution")
plt.xlabel("Words")
plt.ylabel("Frequency")

save_plot("answer_length_histogram.png")

print("\nVisualization completed successfully.")