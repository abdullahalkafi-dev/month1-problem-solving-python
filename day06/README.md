# Day 6: Python Wrap + Warmup Contest

## Today I solved warm-up tasks, two timed problems, and exposed one endpoint

1. Implemented iterator/generator based warm-up utilities
2. Solved first non-repeating character with a two-pass hashmap scan
3. Solved merge sorted arrays using two pointers without sort()
4. Exposed Problem 1 through FastAPI with automatic request validation

This day focused on clean input/output contracts, edge-case testing, and keeping complexity analysis explicit.

## Problems Solved

### 1) First Non-Repeating Character

**What it does:** Returns the first character that appears exactly once in a string.

**Input contract:**
- `s` must be a string

**Output contract:**
- Returns first non-repeating character as `str`
- Returns `""` when no unique character exists

**Examples:**
- `"leetcode"` -> `"l"`
- `"aabb"` -> `""`
- `"swiss"` -> `"w"`

**Approach:**
1. First pass builds frequency map
2. Second pass scans original order and returns first char with count 1

This guarantees correctness because the second pass preserves input order.

### 2) Merge Sorted Arrays (without sort)

**What it does:** Merges two already-sorted integer lists into one sorted list.

**Input contract:**
- `a` must be `list[int]` sorted ascending
- `b` must be `list[int]` sorted ascending

**Output contract:**
- Returns merged sorted `list[int]`

**Examples:**
- `a=[1,3,5], b=[2,4,6]` -> `[1,2,3,4,5,6]`
- `a=[], b=[1,2]` -> `[1,2]`
- `a=[1,1,2], b=[1,3]` -> `[1,1,1,2,3]`

**Approach:**
- Keep two pointers `i`, `j`
- Append smaller value each step
- Append remaining tail when one side ends

## Warm-up Summary

1. `even_number_generator(start, end)` yields even numbers lazily in range
2. `RunningSum(numbers)` iterator returns cumulative sums step-by-step
3. `safe_int_parse(values)` converts valid integer strings and skips invalid inputs safely

## Edge Cases Tested

- Empty input (`""`, `[]`)
- Start greater than end in even generator
- Duplicate-only string for non-repeating character
- Duplicate values during merge
- Invalid data type for merge input
- Invalid API payload type (`{"text": 123}`)

## API Error Strategy

**200 (Success):**
- Valid string payload and successful processing

**422 (Validation Error):**
- Missing `text` field
- `text` is not a string

Validation is handled by Pydantic, so manual schema checks are not needed in the route.

## API Endpoints

- `GET /` - Health/welcome message
- `POST /first-non-repeating` - Solve Problem 1

### FastAPI Request/Response Examples

```json
POST /first-non-repeating
{ "text": "swiss" }
```

```json
{ "result": "w" }
```

```json
POST /first-non-repeating
{ "text": "aabb" }
```

```json
{ "result": "" }
```

## Complexity

### First Non-Repeating Character
- Time: O(n)
- Space: O(n)

### Merge Sorted Arrays
- Time: O(n+m)
- Space: O(n+m)

### Warm-up Utilities
- Even generator: O(k) time for k yielded values, O(1) extra space
- RunningSum iterator: O(n) total, O(1) per next()
- Safe parse: O(n) time, O(v) space for valid parsed items

## Test Run Status

All Day 6 tests pass with pytest and FastAPI TestClient:
- Warm-up tests
- Timed problem tests
- API route tests

## Mistakes Log & Learnings

1. The bug that cost most time was trying to return from frequency-map traversal directly in Problem 1. That can hide ordering mistakes.
2. The fix was enforcing a strict two-pass approach: count first, then scan the original string.
3. For API validation, relying on Pydantic made error handling cleaner and removed repetitive manual checks.

## Reflection

The main win today was combining contest-style problem solving with API exposure. Iterator/generator practice improved clarity around lazy computation, and the two-pointer + two-pass patterns were reliable under edge cases and tests.
