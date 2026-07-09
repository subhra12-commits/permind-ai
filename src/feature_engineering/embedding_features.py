import numpy as np
import pandas as pd

from sentence_transformers import SentenceTransformer

from config import (
    INPUT_DATASET,
    EMBEDDING_FEATURE_FILE,
)

print("=" * 70)
print("SENTENCE EMBEDDING FEATURE ENGINEERING")
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
# Load Embedding Model
# ==========================================================

print("\nLoading embedding model...")

model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)

# ==========================================================
# Generate Embeddings
# ==========================================================

print("Generating embeddings...")

embeddings = model.encode(
    df["combined_text"].tolist(),
    batch_size=32,
    show_progress_bar=True,
    convert_to_numpy=True
)

# ==========================================================
# Save
# ==========================================================

np.save(
    EMBEDDING_FEATURE_FILE,
    embeddings
)

print(f"\nDataset Shape : {df.shape}")
print(f"Embedding Shape : {embeddings.shape}")

print("\nSaved embeddings:")
print(EMBEDDING_FEATURE_FILE)

print("\nEmbedding generation completed successfully.")