from stats import get_num_words
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_dict = count_letters(text)
    list_dict = convert_charact_dict(character_dict)
    list_dict.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    print_report(list_dict)
    print("--- End report ---")


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

def convert_charact_dict(dict):
    dict_list = []
    for key, value in dict.items():
        if key.isalpha():
            new_dict = {}
            new_dict["name"] = key
            new_dict["count"] = value
            dict_list.append(new_dict)
    return dict_list

def sort_on(dict):
    return dict["count"]


def print_report(list):
    for item in list:
        print(f"The '{item["name"]}' character was found {item["count"]} times")


main()
