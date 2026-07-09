import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

from config import (
    INPUT_DATASET,
    TFIDF_FEATURE_FILE,
    TFIDF_VECTORIZER_FILE,
)

print("=" * 70)
print("TF-IDF FEATURE ENGINEERING")
print("=" * 70)

# ==========================================================
# Load Dataset
# ==========================================================

df = pd.read_csv(INPUT_DATASET)

# ==========================================================
# Combine Question + Answer
# ==========================================================

df["combined_text"] = (
    df["processed_question"].fillna("")
    + " "
    + df["processed_answer"].fillna("")
)

# ==========================================================
# TF-IDF Vectorizer
# ==========================================================

vectorizer = TfidfVectorizer(
    max_features=5000,
    ngram_range=(1, 2),
    min_df=2,
    max_df=0.95
)

tfidf_matrix = vectorizer.fit_transform(df["combined_text"])

# ==========================================================
# Save
# ==========================================================

joblib.dump(vectorizer, TFIDF_VECTORIZER_FILE)
joblib.dump(tfidf_matrix, TFIDF_FEATURE_FILE)

print(f"\nDataset Shape      : {df.shape}")
print(f"TF-IDF Shape       : {tfidf_matrix.shape}")
print(f"Vocabulary Size    : {len(vectorizer.vocabulary_)}")

print(f"\nSaved Vectorizer:")
print(TFIDF_VECTORIZER_FILE)

print(f"\nSaved TF-IDF Matrix:")
print(TFIDF_FEATURE_FILE)

print("\nTF-IDF feature engineering completed successfully.")