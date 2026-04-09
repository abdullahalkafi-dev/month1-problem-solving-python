def product_except_self(nums) -> list[int]:
    pre_arr = [1] * len(nums)
    suff_arr = [1] * len(nums)
    for i in range(1, len(nums)):
        pre_arr[i] = pre_arr[i - 1] * nums[i - 1]

    for i in range(len(nums) - 2, -1, -1):
        suff_arr[i] = suff_arr[i + 1] * nums[i + 1]
    final_array = [1] * len(nums)
    for i in range(len(nums)):
        final_array[i] = pre_arr[i] * suff_arr[i]
    return final_array
def product_except_self_optimized(nums) -> list[int]:
    """Calculate product of all elements except self.
    
    Uses space-optimized prefix-suffix technique.
    Result[i] = product of all elements except nums[i].
    """
    n=len(nums)
    res = [1] * n
    for i in range(1, n):
        res[i] = res[i - 1] * nums[i - 1]
    suff = 1
    for i in range(n - 1, -1, -1):
        res[i] = res[i] * suff
        suff = suff * nums[i]
    return res


print(product_except_self_optimized([1, 2, 3, 4]))
print(product_except_self([1, 2, 3, 4]))
