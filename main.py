#define path
book_path = "books/frankenstein.txt"

#print text book
def main():
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

#use a string's .isalpha() method to check if a string only contains characters from the alphabet.
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

#count words
def get_num_words(text):
    words = text.split()
    return len(words)

#Convert dictionary of characters into a list
def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

# and then use the .sort() method.
def sort_on(d):
    return d["num"]

#convert strings to lowercase
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

#count letters
def get_character_sums(text):
    words = text.split()
    return len(words)

#get books
def get_book_text(path):
    with open(book_path) as f:
        return f.read()

main()
