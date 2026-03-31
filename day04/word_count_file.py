def count_words_in_file(path: str) -> dict[str, int]:
    """Read a file and count the frequency of each word.

    Words are lowercased and common punctuation like ',', '.', '!' is removed.
    """
    word_count = {}
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                split_word_list = line.split()
                for word in split_word_list:
                    clean_word = word.strip(",.!").lower()
                    word_count[clean_word] = word_count.get(clean_word, 0) + 1
        return word_count

    except FileNotFoundError:
        print("file was not found")
        return {}
if __name__ == "__main__":
    print(count_words_in_file("./textfile.txt"))