def clamp_score(n: int) -> int:
    """Clamp a score to 0-100 range"""
    if not isinstance(n, int):
        raise TypeError("Only integer is allowed")

    if n < 0:
        return 0
    if n > 100:
        return 100
    return n


print(clamp_score(-10))  # print 0
print(clamp_score(10))  # print 10
print(clamp_score(105))  # print 100
