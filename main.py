def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = count_words(book_text)
    print(f"{word_count} words found in the document")

if __name__ == "__main__":
    main()