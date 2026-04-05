
def count_words(text: str) -> int:
    """Returns the number of space-separated words in the text."""
    return len(text.split())

if __name__=="__main__":
    print(count_words("It's a great day!."))