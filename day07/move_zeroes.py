def move_zeroes(nums: list[int]) -> None:
    """Brute-force approach"""
    new_list = list()
    count_zero = 0
    for i in nums:
        if i == 0:
            count_zero += 1
        else:
            new_list.append(i)
    for i in range(count_zero):
        new_list.append(0)
    nums[:] = new_list




if __name__ == "__main__":
    print(move_zeroes([0, 1, 2, 0, 0, 4, 5, 0]))
