def to_lower_clean(s: str):
    """
    Cleans a string by removing non-alphanumeric characters
    and converting the result to lowercase.
    """
    clean_chars = []
    for char in s:
        if char.isalpha():
            clean_chars.append(char.lower())
    return "".join(clean_chars)


if __name__ == "__main__":
    print(to_lower_clean("Hello World! d@"))
