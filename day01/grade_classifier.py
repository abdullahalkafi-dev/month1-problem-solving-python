def grade_classifier(score: int) -> str:
    """Return grade based on score (0–100)."""

    if not isinstance(score, (int, float)):
        raise TypeError("Score must be a number")
    if not (0 <= score <= 100):
        raise ValueError("Valid range is 0-100")
    score = round(score)
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


if __name__ == "__main__":
    print(grade_classifier(100))  # A
    print(grade_classifier(60))  # D
    print(grade_classifier(89.5))  # B
    # print(grade_classifier(-10.5))  # raise ValueError("Valid range is 0-100")
