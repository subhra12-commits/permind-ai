import joblib
import numpy as np

from config import (
    TFIDF_FEATURE_FILE,
    TFIDF_VECTORIZER_FILE,
    EMBEDDING_FEATURE_FILE,
)

print("=" * 70)
print("FEATURE INSPECTION")
print("=" * 70)

# ==========================================================
# Load TF-IDF
# ==========================================================

print("\nLoading TF-IDF matrix...")

tfidf_matrix = joblib.load(TFIDF_FEATURE_FILE)

print(f"TF-IDF Shape      : {tfidf_matrix.shape}")
print(f"TF-IDF Type       : {type(tfidf_matrix)}")

# ==========================================================
# Load Vectorizer
# ==========================================================

print("\nLoading TF-IDF Vectorizer...")

vectorizer = joblib.load(TFIDF_VECTORIZER_FILE)

print(f"Vocabulary Size   : {len(vectorizer.vocabulary_)}")

feature_names = vectorizer.get_feature_names_out()

print("\nFirst 20 Features:")
print(feature_names[:20])

# ==========================================================
# Load Embeddings
# ==========================================================

print("\nLoading Sentence Embeddings...")

embeddings = np.load(EMBEDDING_FEATURE_FILE)

print(f"Embedding Shape   : {embeddings.shape}")
print(f"Embedding Type    : {embeddings.dtype}")

print("\nFirst Embedding (First 10 Values):")
print(embeddings[0][:10])

print("\nFeature inspection completed successfully.")