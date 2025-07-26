def word_count(text):
    if not text:
        return 0
    words = text.split()
    return len(words)

def character_count(text):
    char_counts = {}
    for char in text:
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

"""
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
    
    """
# Takes a dictionary of characters and their counts, converts it into a sorted list of dictionaries.
def sort_character_counts(char_counts_dict):
    # Convert the input dictionary into a list of dictionaries
    list_of_dicts = []
    for char, count in char_counts_dict.items():
        list_of_dicts.append({"character": char, "count": count})
    # Sort the list of dictionaries by the 'count' value in descending order.
    sorted_list = sorted(list_of_dicts, key=lambda x: x["count"], reverse=True)
    # Print just the key/value pairs from the sorted list of dictionaries.
    for item in sorted_list:
        if isinstance(item['character'], str) and item['character'].isalpha():
            print(f"{item['character']}: {item['count']}")
    return sorted_list

"""
def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
"""