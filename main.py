def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()

def main():
    book_text = get_book_text("frankenstein.txt")
    print(book_text)

if __name__ == "__main__":
    main()
