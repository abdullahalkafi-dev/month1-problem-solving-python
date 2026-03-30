def palindrome_checker(s: str) -> bool:
    """Takes a string and returns True if it is a palindrome by comparing characters in a loop."""

    if not isinstance(s, str):
        raise TypeError("only string is allowed")
    s = s.lower()
    n = len(s)
    for i in range(int(n // 2)):
        print(i, n - 1 - i)
        if s[i] != s[n - 1 - i]:
            return False

    return True


def palindrome_checker_slice(s: str) -> str:
    """Takes a string and returns True if it is a palindrome using string slicing."""
    if not isinstance(s, str):
        raise TypeError("only string is allowed")
    s = s.lower()
    return s == s[::-1]


if __name__ == "__main__":
    print(palindrome_checker("madam"))
    print(palindrome_checker(""))
    print(palindrome_checker_slice("madam"))
    print(palindrome_checker_slice(""))
