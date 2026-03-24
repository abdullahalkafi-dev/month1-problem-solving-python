from typing import Final

VOWELS: Final = {"a", "e", "i", "o", "u"}


def count_vowels(text: str) -> int:
    """Counts the number of vowels in a given string."""

    if not isinstance(text, str):
        raise TypeError("only String allow")
    normalized_text = text.lower()
    count = 0
    for char in normalized_text:
        if char in VOWELS:
            count += 1
    return count


if __name__ == "__main__":
    print(count_vowels("month1-problem-solving-python"))
