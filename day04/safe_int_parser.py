def safe_parse_int(value: str, *, min_value=None, max_value=None) -> int:
    """Convert a string to an integer if possible, otherwise return 0.

    If min_value or max_value are provided, the result is clamped to that range.
    """
    try:
        parsed_value = int(value)
        if min_value is not None and parsed_value < min_value:
            return min_value
        if max_value is not None and parsed_value > max_value:
            return max_value
        return parsed_value
    except (ValueError, TypeError):
        return 0

if __name__ == "__main__":
    print(safe_parse_int("42"))  
    print(safe_parse_int("abc")) 
    print(safe_parse_int("100", max_value=50))

    
    