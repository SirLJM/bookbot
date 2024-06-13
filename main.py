def main():
    path = "books/frankenstein.txt"
    book = read_book(path)
    num_words = count_words(book)
    print(f"{num_words} words found in book")


def read_book(path):
    with open(path) as f:
        return f.read()


def count_words(book):
    words = book.split()
    return len(words)


main()
