def lowercase_unique(words: list[str]) -> list[str]:
    """Takes a list of strings and returns a list of unique lowercase strings, preserving order."""
    seen = set()
    result = [] 
    for word in words:
        w = word.lower()
        if not w in seen:
            seen.add(w)
            result.append(w)
    return result


if __name__ == "__main__":
    print(lowercase_unique(["Apple", "Mango","Banana", "Apple"]))
