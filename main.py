from stats import word_count, character_count, sort_character_counts

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
    file_content = get_book_text("./books/frankenstein.txt")
    number_of_words = word_count(file_content)
    number_of_characters = character_count(file_content.lower())
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
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