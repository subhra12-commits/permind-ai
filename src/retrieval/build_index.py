import faiss
import numpy as np
from pathlib import Path

EMBEDDING_FILE = Path("datasets/features/sentence_embeddings.npy")
INDEX_FILE = Path("datasets/features/faiss_index.index")

print("=" * 70)
print("BUILDING FAISS INDEX")
print("=" * 70)

embeddings = np.load(EMBEDDING_FILE).astype("float32")

# Normalize vectors for cosine similarity
faiss.normalize_L2(embeddings)

dimension = embeddings.shape[1]

index = faiss.IndexFlatIP(dimension)
index.add(embeddings)

faiss.write_index(index, str(INDEX_FILE))

print(f"Embeddings shape : {embeddings.shape}")
print(f"Index vectors    : {index.ntotal}")
print(f"Saved index      : {INDEX_FILE}")
print("\nFAISS index built successfully.")