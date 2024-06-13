def read_book(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def print_book(book):
    print(book)


def count_words(book):
    words = book.split()
    return len(words)


def main():
    path = "books/frankenstein.txt"
    book = read_book(path)
    print_book(book)
    print(count_words(book))


main()
