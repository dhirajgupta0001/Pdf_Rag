import os

from langchain_chroma import Chroma
from model import embeddings
from embedding import embed_chunks


PERSIST_DIRECTORY = "./chroma_db"


def create_vector_store(chunks):
    """
    Create and save the ChromaDB vector store.
    """
    vectors = embed_chunks(chunks)

    texts = [chunk.page_content for chunk in chunks]
    metadatas = [chunk.metadata for chunk in chunks]

    vector_store = Chroma(
        collection_name="alphabet_10k",
        embedding_function=embeddings,
        persist_directory=PERSIST_DIRECTORY
    )

    vector_store.add_texts(
        texts=texts,
        metadatas=metadatas,
        embeddings=vectors
    )

    return vector_store


def load_vector_store():
    """
    Load the existing ChromaDB vector store.
    """
    vector_store = Chroma(
        collection_name="alphabet_10k",
        embedding_function=embeddings,
        persist_directory=PERSIST_DIRECTORY
    )

    return vector_store


def vector_store_exists():
    """
    Check whether the ChromaDB directory already exists.
    """
    return os.path.exists(PERSIST_DIRECTORY)
