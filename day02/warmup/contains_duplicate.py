def contains_duplicate(nums: list[int]):
    """Takes an array of integers and returns True if there are duplicates, otherwise False."""
    seen = set()
    for i in nums:
        if i in seen:
            return True
        seen.add(i)

    return False


if __name__ == "__main__":
    print(contains_duplicate([9, 1, 2, 4, 5, 6, 3]))
