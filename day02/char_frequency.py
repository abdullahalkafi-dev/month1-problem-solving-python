def char_frequency_only_alpha(text: str) -> dict:
    """
    Counts the frequency of each alphabetical character in a string.

    Filters out non-alphabetic characters (numbers, spaces, symbols)
    and ignores case.
    """
    normalizedText = text.lower()
    countDict = {}
    for i in normalizedText:
        if not i.isalpha():
            continue
        if countDict.get(i):
            countDict[i] = countDict[i] + 1
        else:
            countDict[i] = 1
    return countDict


def char_frequency(text: str) -> dict:
    """Counts the frequency of all characters in a string.

    Includes letters, numbers, spaces, and symbols, but ignores case."""

    normalizedText = text.lower()
    countDict = {}
    for i in normalizedText:
        if countDict.get(i):
            countDict[i] = countDict[i] + 1
        else:
            countDict[i] = 1
    return countDict


if __name__ == "__main__":
    char_frequency("Hello00 World!")
    char_frequency_only_alpha("Hello00 World!")
