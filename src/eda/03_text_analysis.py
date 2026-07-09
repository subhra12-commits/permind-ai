import re
from collections import Counter

import nltk
import pandas as pd
from nltk.corpus import stopwords

from utils import load_dataset, save_table, print_header, create_report_folders

create_report_folders()

df = load_dataset()

print_header("TEXT ANALYSIS")

# ==========================================================
# Basic Length Features
# ==========================================================

df["question_word_count"] = (
    df["question"]
    .fillna("")
    .astype(str)
    .apply(lambda x: len(x.split()))
)

df["answer_word_count"] = (
    df["answer"]
    .fillna("")
    .astype(str)
    .apply(lambda x: len(x.split()))
)

df["question_char_count"] = (
    df["question"]
    .fillna("")
    .astype(str)
    .str.len()
)

df["answer_char_count"] = (
    df["answer"]
    .fillna("")
    .astype(str)
    .str.len()
)

# ==========================================================
# Vocabulary Analysis
# ==========================================================

stop_words = set(stopwords.words("english"))

all_text = (
    df["question"].fillna("").astype(str)
    + " "
    + df["answer"].fillna("").astype(str)
)

tokens = []

for sentence in all_text:
    words = re.findall(r"\b[a-zA-Z]+\b", sentence.lower())

    words = [
        word
        for word in words
        if word not in stop_words and len(word) > 2
    ]

    tokens.extend(words)

vocabulary = set(tokens)

word_freq = Counter(tokens)

top_words = pd.DataFrame(
    word_freq.most_common(50),
    columns=["Word", "Frequency"]
)

save_table(top_words, "top_50_words.csv")

# ==========================================================
# Summary Statistics
# ==========================================================

summary = pd.DataFrame({
    "Metric": [
        "Vocabulary Size",
        "Total Tokens",
        "Average Question Length (Words)",
        "Average Answer Length (Words)",
        "Average Question Length (Characters)",
        "Average Answer Length (Characters)",
        "Maximum Question Length",
        "Maximum Answer Length",
        "Minimum Question Length",
        "Minimum Answer Length",
        "Lexical Diversity"
    ],
    "Value": [
        len(vocabulary),
        len(tokens),
        round(df["question_word_count"].mean(), 2),
        round(df["answer_word_count"].mean(), 2),
        round(df["question_char_count"].mean(), 2),
        round(df["answer_char_count"].mean(), 2),
        df["question_word_count"].max(),
        df["answer_word_count"].max(),
        df["question_word_count"].min(),
        df["answer_word_count"].min(),
        round(len(vocabulary) / len(tokens), 4)
    ]
})

save_table(summary, "text_analysis_summary.csv")

# ==========================================================
# Longest Questions
# ==========================================================

longest_questions = (
    df[["question", "question_word_count"]]
    .sort_values(
        by="question_word_count",
        ascending=False
    )
    .head(20)
)

save_table(
    longest_questions,
    "longest_questions.csv"
)

# ==========================================================
# Longest Answers
# ==========================================================

longest_answers = (
    df[["answer", "answer_word_count"]]
    .sort_values(
        by="answer_word_count",
        ascending=False
    )
    .head(20)
)

save_table(
    longest_answers,
    "longest_answers.csv"
)

print(summary)

print("\nTop 10 Most Frequent Words")
print(top_words.head(10))

print("\nText analysis completed successfully.")