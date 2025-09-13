from stats import count_words
from stats import count_characters


def main():
    path = "books/frankenstein.txt"
    book = read_book(path)
    num_words = count_words(book)
    num_characters = count_characters(book)
    print(f"{num_words} words found in the document")
    print(num_characters)

def read_book(path):
    with open(path) as f:
        return f.read()


main()
