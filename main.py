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
    
def word_count(text):
    
    

def main():
    file_content = get_book_text("./books/frankenstein.txt")
    print(file_content)

main()


