import sys
from stats import (
    word_count, 
    character_count, 
    sort_character_counts
)

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)  # Exit with an error code

def get_book_text(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: the specified file at {filepath} was not found.")
        return ""
    except Exception as e:
        print(f"An error occurred while attempting to read the file: {e}")
        return ""

def main():
    file_content = get_book_text(sys.argv[1])
    number_of_words = word_count(file_content)
    number_of_characters = character_count(file_content.lower())
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    sort_character_counts(number_of_characters)
    print("============= END ===============")

main()


