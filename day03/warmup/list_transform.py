def list_transform():
    """
    Generates a list of numbers from 1 to 15, filters for even values,
    and returns a new list containing their squares.
    Returns:
    list: A list of squared even integers [4, 16, 36, 64, 100, 144, 196]."""

    num_list = list(range(5, 16))
    sq = lambda n: n * n
    even_filter = lambda n: n % 2 == 0
    return list(map(sq, filter(even_filter, num_list)))


if __name__ == "__main__":
    print(list_transform())
