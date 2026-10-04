from vector_store import load_vector_store


def get_relevant_chunks(question, k=4):
    """
    Retrieve the most relevant chunks from ChromaDB.
    """
    vector_store = load_vector_store()

    results = vector_store.similarity_search(
        question,
        k=k
    )

    return results
