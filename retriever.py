
from vector_store import create_vector_store


def get_relevant_chunks(chunks, question, k=4):
    """
    Retrieve the most relevant chunks for a question.
    """
    vector_store = create_vector_store(chunks)

    results = vector_store.similarity_search(
        question,
        k=k
    )

    return results
