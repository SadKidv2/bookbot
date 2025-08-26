from stats import get_num_words, get_character_count

def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = get_num_words(book_text)
    char_count = get_character_count(book_text)
    
    print(f"{word_count} words found in the document")
    print(char_count)

if __name__ == "__main__":
    main()