from semantic_search import SemanticSearchEngine

engine = SemanticSearchEngine()

query = input("Enter your interview question: ")

results = engine.search(query, top_k=5)

print("\nTop Results:")
print("=" * 70)

for i, result in enumerate(results, start=1):
    print(f"\nResult {i}")
    print(f"Score      : {result['score']:.4f}")
    print(f"Category   : {result['category']}")
    print(f"Difficulty : {result['difficulty']}")
    print(f"Dataset    : {result['dataset_name']}")
    print(f"Question   : {result['question']}")
    print(f"Answer     : {result['answer']}")