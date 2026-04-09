# Day 8: Sliding Window + Array Optimization

Today focused on two efficient techniques: sliding window for finding optimal subarrays, and prefix-suffix products for array calculations.

I solved two main problems and four warm-up tasks using window-sliding and prefix-suffix approaches.

## Problems Solved

### 1) Minimum Subarray Length

**What it does:** Find the smallest subarray with sum >= target value.

**How it works:**
- Start with left and right pointers at beginning
- Expand window by moving right pointer and adding elements
- When sum reaches target, shrink window from left to find minimum length
- Track the smallest valid window size

**Examples:**
- `min_subarray_len(7, [2, 3, 1, 2, 4, 3])` → `2` (subarray [4, 3])
- `min_subarray_len(4, [1, 4, 4])` → `1` (just [4])
- `min_subarray_len(15, [1, 1, 1])` → `inf` (no valid subarray)

### 2) Product Except Self

**What it does:** For each element, calculate product of all other elements.

**How it works:**
1. First pass: calculate prefix products moving left to right
2. Second pass: calculate suffix products moving right to left
3. Combine prefix and suffix for final result at each position

**Examples:**
- `[1, 2, 3, 4]` → `[24, 12, 8, 6]`
- `[2, 3, 4, 5]` → `[60, 40, 30, 24]`

**Optimization:** Uses O(1) extra space (reuses output array for intermediate calculations).

## Warm-up Tasks

### 1) First Window Sum
Calculate sum of first k consecutive elements.

### 2) Max Sum Subarray of Size K
Find the maximum sum among all windows of size k using sliding window.

### 3) Range Sum
Calculate sum of elements between two indices (inclusive).

### 4) Max Average Subarray
Find average of the subarray with size k that has maximum sum.

## Complexity Analysis

- **Minimum Subarray Length:** O(n) time, O(1) space (each element visited max twice)
- **Product Except Self:** O(n) time, O(1) extra space (output array doesn't count)
- **First Window Sum:** O(k) time, O(1) space
- **Max Sum Subarray K:** O(n) time, O(1) space
- **Range Sum:** O(n) time, O(1) space
- **Max Average Subarray:** O(n) time, O(1) space

## Key Learning

Both approaches avoid wasteful recomputation:
- **Sliding Window:** Remove old values and add new ones instead of recalculating sums
- **Prefix-Suffix:** Build reusable products in two passes instead of recalculating for each position

Main takeaway: precompute or reuse intermediate results when processing sequences.
