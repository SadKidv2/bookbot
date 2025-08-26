from stats import get_num_words, get_character_count, print_report

def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = get_num_words(book_text)
    char_count = get_character_count(book_text)
    report = print_report(char_count)
    
    print(f"Found {word_count} total words")
    print(f"e: {char_count.get('e', 0)}")  
    print(f"t: {char_count.get('t', 0)}")

if __name__ == "__main__":
    main()