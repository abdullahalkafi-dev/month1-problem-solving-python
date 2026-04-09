def min_subarray_len(target, nums) -> int:
    """Find minimum length of subarray with sum >= target.
    
    Uses sliding window technique to track contiguous elements.
    Returns smallest subarray length, or inf if no match found.
    """
    l = 0

    min_len = float("inf")
    curr_sum = 0
    for r in range(len(nums)):
        curr_sum += nums[r]
        while curr_sum >= target:
            min_len = min(min_len, r - l + 1)
            curr_sum -= nums[l]
            l += 1
    return min_len


if __name__ == "__main__":
    print(min_subarray_len(7, [2, 3, 1, 2, 4, 3]))
