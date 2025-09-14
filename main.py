import sys

from stats import count_words
from stats import count_characters
from stats import sort_counted_characters


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
    book = read_book(path)
    num_words = count_words(book)
    sorted_chars = sort_counted_characters(count_characters(book))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at: {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char, count in sorted_chars:
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

def read_book(path):
    with open(path) as f:
        return f.read()


main()
