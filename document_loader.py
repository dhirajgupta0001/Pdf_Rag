from langchain_community.document_loaders import PyPDFLoader

def load_pdf(file_path):
    """
    Load a PDF and return its pages
    as LangChain Document objects.
    """
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    print(f"Loaded {len(documents)} pages")

    return documents
