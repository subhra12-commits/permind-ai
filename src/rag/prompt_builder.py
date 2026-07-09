def build_interview_prompt(user_question, retrieved_results):
    context_blocks = []

    for i, result in enumerate(retrieved_results, start=1):
        context_blocks.append(
            f"""
Context {i}
Question: {result['question']}
Answer: {result['answer']}
Category: {result['category']}
Difficulty: {result['difficulty']}
"""
        )

    context = "\n".join(context_blocks)

    prompt = f"""
You are an AI Interview Coach.

Use the retrieved interview context below to answer the user's question clearly and professionally.

User Question:
{user_question}

Retrieved Context:
{context}

Instructions:
- Give a direct and beginner-friendly answer.
- Use the retrieved context as the main source.
- If useful, add a short example.
- Keep the answer suitable for interview preparation.
- Do not mention that you are using retrieved context.

Final Answer:
"""

    return prompt