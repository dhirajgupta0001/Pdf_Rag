from document_loader import load_pdf
from text_splitter import split_documents
from vector_store import create_vector_store, vector_store_exists
from rag import ask_question

PDF_PATH = "data/alphabet_2022_10k.pdf"


def main():

    # Create the vector database only if it doesn't already exist
    if not vector_store_exists():

        print("Creating vector database...")

        documents = load_pdf(PDF_PATH)

        chunks = split_documents(documents)

        create_vector_store(chunks)

        print("Vector database created.")

    else:
        print("Existing vector database found.")


    print("\nAlphabet 2022 10-K RAG Assistant")
    print("Type 'exit' to quit.\n")

    while True:

        question = input("Your question: ")

        if question.lower().strip() == "exit":
            print("Goodbye!")
            break

        answer = ask_question(question)

        print("\nAnswer:")
        print(answer)
        print()


if __name__ == "__main__":
    main()
