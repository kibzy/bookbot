def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_dict = count_letters(text)
    print(f"{num_words} words found in the document")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_letters(string):
    letter_dict = dict()
    for letter in string:
        lowered_letter = letter.lower()
        if lowered_letter in letter_dict:
            letter_dict[lowered_letter] += 1
        else:
            letter_dict[lowered_letter] = 1
    # print(letter_dict)
    return letter_dict
main()
