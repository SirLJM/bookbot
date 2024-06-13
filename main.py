def print_book(book):
    with open(book) as f:
        file_contents = f.read()
    print(file_contents)


def main():
    book = "books/frankenstein.txt"
    print_book(book)


main()
