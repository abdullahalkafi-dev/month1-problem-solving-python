def first_window_sum(arr, k) -> int:
    """Calculate sum of first k elements in array."""
    if k <= 0:
        raise ValueError("Window size k must be positive.")
    if k > len(arr):
        raise ValueError("Window size k cannot exceed array length.")
    sum_k = 0
    for i in range(k):
        sum_k = sum_k + arr[i]
    return sum_k


def max_sum_subarray_k(arr, k) -> int:
    """Find maximum sum of any subarray with length k using sliding window."""
    if k <= 0:
        raise ValueError("Window size k must be positive.")
    if k > len(arr):
        raise ValueError("Window size k cannot exceed array length.")

    current = 0

    for i in range(k):
        current += arr[i]

    max_sum = current
    for i in range(1, len(arr) - k + 1):
        current = current - arr[i - 1] + arr[i + k - 1]
        if current > max_sum:
            max_sum = current
    return max_sum


def range_sum(arr, l, r) -> int:
    """Calculate sum of elements in range [l, r] (inclusive)."""
    n = len(arr)
    if n == 0:
        raise ValueError("Array is empty.")
    if l < 0 or r >= n:
        raise ValueError("Out of bounds.")
    if l > r:
        raise ValueError("Left index cannot be greater than right index.")

    total = 0

    for i in range(l, r + 1):
        total += arr[i]

    return total

def max_average_subarray(arr, k) -> float:
    """Find average of subarray with length k that has maximum sum."""
    if k <= 0:
        raise ValueError("Window size k must be positive.")
    if k > len(arr):
        raise ValueError("Window size k cannot exceed array length.")

    current = 0

    for i in range(k):
        current += arr[i]

    max_sum = current
    for i in range(1, len(arr) - k + 1):
        current = current - arr[i - 1] + arr[i + k - 1]
        if current > max_sum:
            max_sum = current
    return max_sum / k


    
    
    




if __name__ == "__main__":
    print(first_window_sum([2,1,5,1,3,2],3))
    print(max_sum_subarray_k([2, 1, 5, 1, 3, 2], 3))
    print(max_sum_subarray_k([-1, -2, -3], 2))
    print(range_sum([1, 2, 3, 4, 5], 1, 3))
    print(range_sum([10], 0, 0))
    print(max_average_subarray([2, 1, 5, 1, 3, 2], 3))