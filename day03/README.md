# Day 3 : Factorial & Palindrome Checker

## Today I solved two core Python logic problems

	1. Factorial using loop and recursion
	2. Palindrome checking using loop and slicing

Today felt smooth overall. I got factorial in the first try.
Palindrome was also easy to understand, but it took more time to finish correctly.

## Problems Solved

### 1) Factorial

I solved factorial in two ways:

- `factorial_loop(n)`: uses a `for` loop from 2 to `n`
- `factorial_recursion(n)`: uses recursion with base cases

Validation:

- non-integer input => `TypeError`
- negative input => `ValueError`

Base cases:

- `0! = 1`
- `1! = 1`

### 2) Palindrome Checker

I solved palindrome in two ways:

- `palindrome_checker(s)`: compares characters from both ends using a loop
- `palindrome_checker_slice(s)`: checks `s == s[::-1]`

Validation:

- non-string input => `TypeError`

Behavior:

- Works with uppercase/lowercase by converting to lowercase first
- Empty string returns `True`
- Phrases like `"Step on no pets"` return `True`

## My Palindrome Journey

Palindrome did not fail hard, but it took a few tries to make it clean.

What happened:

1. First, I tried a two-pointer style with extra variables (`i`, `j`, flag, manual updates).
2. Then I simplified it to one loop with index math.
3. Finally, I fixed the half-range logic with `n // 2`, and it became clean and reliable.

Main learning:

- Off-by-one mistakes are common in palindrome loops.
- `n // 2` is the safest and cleanest boundary for mirror comparison.
- Keeping the loop simple is better than over-managing pointers.

## Mistakes Log & Learnings

	1. In my early palindrome attempt, I used extra pointer updates and a flag variable, which made the logic harder to track.
	2. I also experimented with a loop boundary that was not clean enough, which can cause confusion in middle-index handling.
	3. I refactored to a minimal loop (`for i in range(n // 2)`) and direct mirrored comparison. That made the code easy and stable.
	4. For factorial, I got it right on the first try because base cases (`0`, `1`) and input checks were clear before coding.

## Complexity

### Factorial

- Time: `O(n)`
- Space:
	- loop version: `O(1)`
	- recursion version: `O(n)` call stack

### Palindrome

- loop version: Time `O(n)`, Space `O(1)`
- slicing version: Time `O(n)`, Space `O(n)` (creates reversed copy)

## Workflow Reflection

Today I followed:
code -> test -> simplify -> verify

Big win today: factorial was done in first try.
Big learning today: palindrome is simple in concept, but clean indexing takes a little patience.

## Test Run Status

All current Day 3 tests passed in local execution using `pytest`.
