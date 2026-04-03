def first_non_repeating_char(s: str) -> str:
    if not isinstance(s, str):
        raise TypeError("s data type not allowed")

    frequency_map = {}
    for char in s:
        frequency_map[char] = frequency_map.get(char, 0) + 1

    for char in s:
        if frequency_map[char] == 1:
            return char

    return ""


def merge_sorted(a: list[int], b: list[int]) -> list[int]:
    if not isinstance(a, list):
        raise TypeError("a data type not allowed")
    if not isinstance(b, list):
        raise TypeError("b data type not allowed")

    for value in a:
        if not isinstance(value, int):
            raise TypeError("a item data type not allowed")
    for value in b:
        if not isinstance(value, int):
            raise TypeError("b item data type not allowed")

    result = []
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i = i + 1
        else:
            result.append(b[j])
            j = j + 1

    result.extend(a[i:])
    result.extend(b[j:])

    return result
