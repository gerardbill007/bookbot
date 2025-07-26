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

"""
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(f"{num_words} words found in the document")
    print(chars_dict)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    

main()
"""
"""
from stats import (
    get_num_words,
    chars_dict_to_sorted_list,
    get_chars_dict,
)


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print_report(book_path, num_words, chars_sorted_list)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()
"""