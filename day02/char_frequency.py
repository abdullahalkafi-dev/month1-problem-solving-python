def char_frequency_only_alpha(text: str) -> dict:
    """
    Counts the frequency of each alphabetical character in a string.

    Filters out non-alphabetic characters (numbers, spaces, symbols)
    and ignores case.
    """
    normalizedText = text.lower()
    countDict = {}
    for i in normalizedText:
        if i.isalpha():
            countDict[i] = countDict.get(i, 0) + 1

    return countDict


def char_frequency(text: str) -> dict:
    """Counts the frequency of all characters in a string.

    Includes letters, numbers, spaces, and symbols, but ignores case."""

    normalizedText = text.lower()
    countDict = {}
    for i in normalizedText:

        countDict[i] = countDict.get(i, 0) + 1

    return countDict


if __name__ == "__main__":
    print(char_frequency("Hello00 World!"))
    print(char_frequency_only_alpha("Hello00 World!"))
