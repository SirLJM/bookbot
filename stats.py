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

def sort_counted_characters(chars):
    return sorted(chars.items(), key=lambda x: x[1], reverse=True)