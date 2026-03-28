def deduplicate(data: list[int]) -> list[int]:
    """
    Removes duplicates from a list but keeps the original order.

    1. It tracks what it has already seen.
    2. If a number is new, it adds it to the result.
    3. If a number is a repeat, it skips it.
    """
    seen = set()
    orderedResult = []
    for i in data:
        if not i in seen:
            seen.add(i)
            orderedResult.append(i)

    return orderedResult


print(deduplicate([3, 1, 3, 2, 1, 5, 2]))
