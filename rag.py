
from model import model
from retriever import get_relevant_chunks


def ask_question(chunks, question):
    """
    Answer a question using retrieved context from the PDF.
    """
    relevant_chunks = get_relevant_chunks(chunks, question)

    context = "\n\n".join(
        chunk.page_content for chunk in relevant_chunks
    )

    prompt = f"""
You are an assistant answering questions about Alphabet's 2022 10-K.

Use only the context below to answer the question.
If the context does not contain the answer, say you don't
have enough information.

Context:
{context}

Question:
{question}

Answer:
"""

    response = model.invoke(prompt)

    return response.content
