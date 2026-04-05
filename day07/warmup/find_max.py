def find_max(num_list: list[int]) -> int:
    """Returns the maximum integer from the list."""
    if not num_list:
        raise ValueError("List must not be empty")
    max_num = num_list[0]
    for i in num_list:
        if not isinstance(i, int):
            raise TypeError("Only integers allowed")
        if i > max_num:
            max_num = i
    return max_num


if __name__ == "__main__":
    print(find_max([10, 1, 2, 3, 4, 5, 6, 7, 8, 0]))
