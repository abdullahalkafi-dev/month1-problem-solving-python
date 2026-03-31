def count_words_in_a_line(s: str) -> dict:
    """Count each word in a line and return a frequency dictionary.

    Words are lowercased and common punctuation like ',', '.', '!' is removed.
    """
    print(s)
    data = {}
    split_word_list = s.split()
    for word in split_word_list:
        clean_word = word.strip(",.!").lower()
        data[clean_word] = data.get(clean_word, 0) + 1

    return data


if __name__ == "__main__":
    print(count_words_in_a_line("hello world my boy. hello to   all"))
