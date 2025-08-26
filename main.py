import sys

def get_character_count(text):
    # Convert to lowercase to avoid duplicates
    text_lower = text.lower()
    
    # Create a dictionary to count characters
    char_count = {}
    
    # Count each character
    for char in text_lower:
        if char.isalpha():  # Only include alphabetical characters
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
    return char_count

def print_report(char_count):
    # Convert to list of dictionaries for sorting
    char_list = []
    for char, count in char_count.items():
        char_list.append({"char": char, "num": count})
    
    # Sort by count (descending) using the "num" key
    char_list.sort(key=lambda x: x["num"], reverse=True)
    
    for item in char_list:
        print(f"{item['char']}: {item['num']}")

def get_num_words(text):
    return len(text.split())

def main():
    # Check if we have the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Get the book file path from command line arguments
    book_path = sys.argv[1]
    
    try:
        # Open and read the book file
        with open(book_path, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Get character count dictionary
        char_count = get_character_count(text)
        
        # Print the character frequency report
        print_report(char_count)
        
    except FileNotFoundError:
        print(f"❌ Error: Could not find the file '{book_path}'")
        print("Please check that the file path is correct and the file exists.")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()