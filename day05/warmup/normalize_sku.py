import re


def normalize_sku(raw: str) -> str:
    if not isinstance(raw, str):
        raise TypeError("Input must be an string")
    if len(raw) == 0:
        raise ValueError("Empty string is not allowed")
    if re.search(r"\s", raw):
        raise ValueError("Spaces is not allow in sku")
    return raw.upper()


if __name__ == "__main__":
    print(normalize_sku("ab-12"))
    print(normalize_sku(""))
    print(normalize_sku(" "))
