# Day 4: File Operations & Word Frequency

## Today I solved two file and string processing problems

1. Counting lines in a file by sentence boundaries
2. Counting word frequency in a string with cleaning

No API today — just focused on file I/O and data cleaning.

## Problems Solved

### 1) Count File Lines

**What it does:** Reads a text file and counts how many sentences (lines) it has.

- Splits content by sentence endings: `.`, `?`, `!`
- Strips whitespace from each line
- Ignores empty strings after split

**Key learning:** The `re.split(r"[.?!]", content)` pattern splits on multiple delimiters at once.

```python
lines = [s.strip() for s in raw_lines if s.strip()]
```

This one-liner filters to keep only non-empty lines and removes extra whitespace.

**Error handling:** Catches `FileNotFoundError` if the file doesn't exist.

### 2) Count Words in a Line

**What it does:** Takes a string and returns a dictionary of word frequencies.

```python
clean_word = word.strip(",.!").lower()
data[clean_word] = data.get(clean_word, 0) + 1
```

**Key cleaning steps:**
- Strip punctuation: `.`, `,`, `!`
- Convert to lowercase for case-insensitive counting
- Use `dict.get(key, 0) + 1` to increment counts

**Example:**
```
Input: "hello world my boy. hello to all"
Output: {'hello': 2, 'world': 1, 'my': 1, 'boy': 1, 'to': 1, 'all': 1}
```

## Complexity

### Count File Lines
- Time: O(n) — Read the file once, split once, filter once
- Space: O(n) — Store all lines in memory

### Count Words in a Line
- Time: O(n) — Iterate through each word exactly once
- Space: O(k) — Where k is the number of unique words

## Key Insight: Why Not O(n²)?

The loops are **collaborative**, not nested in the traditional sense:
- Each word is visited exactly once across the entire program
- Total iterations = total words in the file, not (words × lines)
- This stays **O(n)** because the work is distributed, not repeated

To make it O(n²), you'd need to re-scan the entire file for every word.
