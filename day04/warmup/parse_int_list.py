def parse_int_list(int_list: list) -> list[int]:
    """Convert valid values from a list into integers.

    Skips values that cannot be converted and ignores booleans.
    """
    parse_list = []
    for i in int_list:
        if isinstance(i, bool):
            continue
        try:
            parse_list.append(int(i))
        except (ValueError, TypeError):
            continue
    return parse_list


if __name__ == "__main__":
    print(parse_int_list(["22", "a", "10", "!", True]))
