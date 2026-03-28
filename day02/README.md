# Day 2 : Character Frequency & Deduplication

## Today I solved two core Python data structure problems

    1. Character frequency counting using hash maps (dictionaries)
    2. Order-preserving deduplication using a combination of sets and lists

I also took these utility functions and exposed them as web endpoints using FastAPI to see how they would work in a real backend environment.

## Problems Solved

### 1) Character Frequency

Input: string  
Output: dictionary with character counts

- Two versions created:
    - `char_frequency()`: Normalizes everything to lowercase and counts all characters (including symbols and spaces).
    - `char_frequency_only_alpha()`: Normalizes to lowercase and ignores spaces, digits, and symbols using `.isalpha()`.

Pattern used: `countDict[i] = countDict.get(i, 0) + 1` (One-pass hash map).

### 2) Deduplicate While Preserving Order

Input: list of mixed items  
Output: list with duplicates removed, original order kept intact.

Pattern used: **Seen set + Output list**.
- A `set()` tracks what has already been seen (giving O(1) fast lookups).
- A `list()` keeps the exact order.
- If we just used `list(set(data))`, we would lose the original order.

## API Integration

I set up a FastAPI backend to expose these utilities as POST endpoints:
- Built `TextData` models using Pydantic.
- Included validation: throws a HTTP 400 error if empty text is supplied.
- Mapped `/char-frequency-all` and `/char-frequency-alpha` to return the dictionary counts as JSON.

## Mistakes Log & Learnings

    1. Initially, I wrote a verbose `if/else` block to check if a character existed in the dictionary before incrementing.
    2. I learned that using `dict.get(key, 0) + 1` simplifies the code into a single, clean, Pythonic line and avoids bugs.
    3. Learned why data structure choice matters: `set` for O(1) membership checks, `dict` for counting mapping, and `list` for sequence order.

## Complexity

### Character Frequency
- Time: O(n) - We iterate through the string exactly once.
- Space: O(k) - Where k is the number of unique characters stored in the dictionary.

### Deduplicate (Preserve Order)
- Time: O(n) average - We iterate through the list once, and checking a `set` is O(1) on average.
- Space: O(n) - In the worst case (all unique items), both the list and the set store all items.

## Test Run Status

All current Day 2 tests passed via standard Python local execution, and the Uvicorn FastAPI server is running successfully!
