
from langchain_chroma import Chroma
from model import embeddings
from embedding import embed_chunks


def create_vector_store(chunks, persist_directory="./chroma_db"):
    """
    Store text chunks and their embeddings in ChromaDB.
    """
    vectors = embed_chunks(chunks)

    texts = [chunk.page_content for chunk in chunks]
    metadatas = [chunk.metadata for chunk in chunks]

    vector_store = Chroma(
        collection_name="alphabet_10k",
        embedding_function=embeddings,
        persist_directory=persist_directory
    )

    vector_store.add_texts(
        texts=texts,
        metadatas=metadatas,
        embeddings=vectors
    )

    return vector_store
