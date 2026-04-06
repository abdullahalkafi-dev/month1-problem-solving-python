def move_zeroes_brute(nums: list[int]) -> None:
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


def move_zeroes_two_pointers(nums: list[int]) -> None:
    """Two pointers approach"""
    length = len(nums)
    write_index = 0
    for real_index in range(length):
        if not nums[real_index] == 0:
            nums[write_index] = nums[real_index]
            write_index += 1

    for i in range(write_index, length):
        nums[i] = 0


if __name__ == "__main__":
    print(move_zeroes_brute([0, 1, 2, 0, 0, 4, 5, 0]))
    print(move_zeroes_two_pointers([0, 1, 2, 0, 0, 4, 5, 0]))
