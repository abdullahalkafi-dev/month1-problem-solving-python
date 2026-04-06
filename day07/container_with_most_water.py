def max_area(heights: list[int]) -> int:
    """Finds the maximum area of water that can be trapped between two vertical lines."""
    left, right = 0, len(heights) - 1
    max_area_size = 0

    while left < right:
        width = right - left
        current_height = min(heights[left], heights[right])
        area = width * current_height
        max_area_size = max(max_area_size, area)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_area_size


if __name__ == "__main__":
    print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
