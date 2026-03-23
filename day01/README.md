# Day 1 : FizzBuzz Variant & Grade Classifier

## Today I solved two core Python logic problems

    1. FizzBuzz variant with an extra rule for multiples of 7
    2. Grade classifier with validation and boundary handling

I focused on writing pure functions and validating behavior with test assertions.

## Problems Solved

### 1) FizzBuzz Variant

Rule summary for one number:

- multiple of 3 => Fizz
- multiple of 5 => Buzz
- multiple of 7 => Pop
- combine labels when multiple conditions match
- if no condition matches, return the number as string

Examples:

- 14 => Pop
- 15 => FizzBuzz
- 105 => FizzBuzzPop
- 1 => "1"

### 2) Grade Classifier

Input: numeric score in range 0 to 100  
Output:

- 90 to 100 => A
- 80 to 89 => B
- 70 to 79 => C
- 60 to 69 => D
- below 60 => F

Validation:

- non-numeric input => TypeError
- score outside 0 to 100 => ValueError

Note: score is rounded before classification.

## Boundary Cases Tested

### FizzBuzz

- 1 (no label)
- 0 (divisible by 3, 5, and 7)
- 3, 5, 14 (single labels)
- 15 (combined label)
- 105 (all labels combined)

### Grade

- 100 (top boundary)
- 70 and 79 (C boundary band)
- 69 (D boundary)
- 10 (low score => F)
- decimal boundary behavior: 89.4 => B, 89.5 => A (after rounding)

## Mistakes Log (Updated)

    1. At first, I only accepted `int` for score input.
    2. Then I realized scores can be decimal values, so I updated validation to accept both `int` and `float`, and improved the error message.
    3. I was initially missing `round()`, which caused boundary issues for decimal inputs (for example, 89.5).
    4. In FizzBuzz, I first wrote hardcoded checks like "if 15" or "if 105". That approach was not scalable and could introduce bugs when adding new rules.
    5. I refactored to a composable string-building approach (`result += ...`), which is cleaner, more scalable, and easier to extend.

### FizzBuzz Function (single value version)

- Time: O(1)
- Space: O(1)
- Reason: fixed number of modulus checks and string concatenations.

### Grade Classifier

- Time: O(1)
- Space: O(1)
- Reason: fixed set of condition checks.

## Workflow Reflection

Today I followed:
code -> test -> verify boundaries -> reflect

This helped me find edge-case behavior quickly, especially decimal rounding in grade classification.

## Test Run Status

All current Day 1 tests passed in local execution.
