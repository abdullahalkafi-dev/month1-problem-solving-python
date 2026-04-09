from day08.sliding_window_fixed import min_subarray_len
from day08.prefix_suffix import product_except_self_optimized
from day08.warmup.warmup_day08 import first_window_sum, max_sum_subarray_k, range_sum, max_average_subarray


def test_min_subarray_len():
    assert min_subarray_len(7, [2, 3, 1, 2, 4, 3]) == 2
    assert min_subarray_len(4, [1, 4, 4]) == 1
    assert min_subarray_len(15, [1, 1, 1]) == float("inf")


def test_product_except_self_optimized():
    assert product_except_self_optimized([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self_optimized([2, 3, 4, 5]) == [60, 40, 30, 24]
    assert product_except_self_optimized([5]) == [1]


def test_first_window_sum():
    assert first_window_sum([2, 1, 5, 1, 3, 2], 3) == 8
    assert first_window_sum([1, 2, 3, 4, 5], 2) == 3
    assert first_window_sum([10], 1) == 10


def test_max_sum_subarray_k():
    assert max_sum_subarray_k([2, 1, 5, 1, 3, 2], 3) == 9
    assert max_sum_subarray_k([1, 2, 3, 4, 5], 3) == 12
    assert max_sum_subarray_k([-1, -2, -3], 2) == -3


def test_range_sum():
    assert range_sum([1, 2, 3, 4, 5], 1, 3) == 9
    assert range_sum([10], 0, 0) == 10
    assert range_sum([1, 2, 3, 4], 0, 3) == 10


def test_max_average_subarray():
    result = max_average_subarray([2, 1, 5, 1, 3, 2], 3)
    assert abs(result - 3.0) < 0.01
    result = max_average_subarray([1, 2, 3, 4, 5], 2)
    assert abs(result - 4.5) < 0.01


if __name__ == "__main__":
    test_min_subarray_len()
    test_product_except_self_optimized()
    test_first_window_sum()
    test_max_sum_subarray_k()
    test_range_sum()
    test_max_average_subarray()
    print("All tests passed!")
