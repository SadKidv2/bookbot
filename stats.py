def get_num_words(text):
    words = text.split()
    return len(words)
def get_character_count(text):
    # Convert to lowercase to avoid duplicates
    text_lower = text.lower()
    
    # Create a dictionary to count characters
    char_count = {}
    
    # Count each character
    for char in text_lower:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count