from pathlib import Path

INPUT_DATASET = Path("datasets/final/preprocessed_interview_dataset.csv")

FEATURES_DIR = Path("datasets/features")
FEATURES_DIR.mkdir(parents=True, exist_ok=True)

TFIDF_FEATURE_FILE = FEATURES_DIR / "tfidf_features.pkl"
TFIDF_VECTORIZER_FILE = FEATURES_DIR / "tfidf_vectorizer.pkl"

EMBEDDING_FEATURE_FILE = FEATURES_DIR / "sentence_embeddings.npy"