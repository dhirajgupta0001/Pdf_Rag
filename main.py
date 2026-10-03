
from document_loader import load_pdf
from text_splitter import split_documents
from rag import ask_question


PDF_PATH = "/Users/dhirajgupta/Downloads/laws-of-cricket-2017-code-3rd-edition-2022_1.pdf"


def main():
    # Load the PDF
    documents = load_pdf(PDF_PATH)

    # Split pages into chunks
    chunks = split_documents(documents)

    # Ask questions
    print("\nLaw of Cricket.")
    print("Type 'exit' to quit.\n")

    while True:
        question = input("Your question: ")

        if question.lower().strip() == "exit":
            print("Goodbye!")
            break

        answer = ask_question(chunks, question)

        print("\nAnswer:")
        print(answer)
        print()


if __name__ == "__main__":
    main()
