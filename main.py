def main():
    path = "books/frankenstein.txt"
    book = read_book(path)
    num_words = count_words(book)
    print(f"{num_words} words found in book")
    print(count_characters(book))


def read_book(path):
    with open(path) as f:
        return f.read()


def count_words(book):
    words = book.split()
    return len(words)


def count_characters(book):
    chars = {}
    lower_case = book.lower()
    for char in lower_case:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars


main()
