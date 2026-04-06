# Day 7: Arrays + Two Pointers Practice

Today was all about solving classic array/string problems and practicing clean logic.

I worked on:
1. Two Sum (brute-force and hash map)
2. Valid Palindrome (ignore non-alphanumeric, case-insensitive)
3. Move Zeroes (brute-force and in-place two pointers)
4. Container With Most Water (two pointers)

I also completed three warm-up tasks:
- `count_words(text)`
- `find_max(num_list)`
- `sum_even(num_list)`

## What I solved

### 1) Two Sum

Implemented two versions:
- `two_sum_brute`: checks every pair
- `two_sum_hash`: stores seen values in a hash map for faster lookup

If no valid pair is found, both versions raise `ValueError`.

### 2) Valid Palindrome

Used left/right pointers.
- Skip non-alphanumeric characters
- Compare lowercase characters
- Return `True` only if full string matches palindrome rules

### 3) Move Zeroes

Implemented two approaches:
- `move_zeroes_brute`: builds a new list, then writes back
- `move_zeroes_two_pointers`: in-place write index method

The two-pointer version keeps order of non-zero values and avoids extra list creation.

### 4) Container With Most Water

Used two pointers from both ends:
- Compute area each step
- Move the pointer at the shorter height
- Track maximum area seen so far

This gives an efficient linear-time solution.

## Warm-up notes

- `count_words`: simple split-based word count
- `find_max`: finds max with input validation (raises on empty list or non-int values)
- `sum_even`: sums only even integers and validates element types

## Complexity

- Two Sum (brute): O(n^2) time, O(1) space
- Two Sum (hash): O(n) time, O(n) space
- Valid Palindrome: O(n) time, O(1) space
- Move Zeroes (brute): O(n) time, O(n) extra space
- Move Zeroes (two pointers): O(n) time, O(1) extra space
- Container With Most Water: O(n) time, O(1) space

## Reflection

Today helped me see a clear pattern:
- Brute-force helps understand the problem first
- Two pointers and hash maps reduce time complexity a lot
- Small design choices (in-place vs extra list) matter for space efficiency

Main takeaway: solve correctly first, then optimize with a clear reason.
