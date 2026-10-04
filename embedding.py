from model import embeddings

def embed_chunks(chunks):
    """
    Convert text chunks into numerical vectors.
    """
    texts = [chunk.page_content for chunk in chunks]

    vectors = embeddings.embed_documents(texts)

    return vectors
