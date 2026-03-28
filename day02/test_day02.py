from char_frequency import char_frequency, char_frequency_only_alpha
from deduplicate_order import deduplicate

def test_char_frequency_suite():
    # Test: Basic strings & Case sensitivity
    assert char_frequency("Aa") == {"a": 2}
    assert char_frequency("Hello") == {"h": 1, "e": 1, "l": 2, "o": 1} 
    # Test: Numbers and Symbols (Included)
    assert char_frequency("11 !!") == {"1": 2, " ": 1, "!": 2}
    # Test: Empty string
    assert char_frequency("") == {}
    
    print("✅ All char_frequency tests passed!")

def test_char_frequency_only_alpha_suite():
    # Test: Filters out non-alpha
    assert char_frequency_only_alpha("Hi 123!") == {"h": 1, "i": 1}
    
    # Test: Mixed Case (Normalized)
    assert char_frequency_only_alpha("AbA") == {"a": 2, "b": 1}
    
    # Test: String with zero alphabetic characters
    assert char_frequency_only_alpha("12345!@#") == {}
    
    # Test: Empty string
    assert char_frequency_only_alpha("") == {}

    print("✅ All char_frequency_only_alpha tests passed!")


def test_deduplicate():
    # Standard case: maintain order and remove duplicates
    assert deduplicate([3, 1, 3, 2, 1, 5, 2]) == [3, 1, 2, 5]
    
    # Already unique: should return the same list
    assert deduplicate([1, 2, 3]) == [1, 2, 3]
    
    # All duplicates: should return just one instance
    assert deduplicate([7, 7, 7, 7]) == [7]
    
    # Empty list: should return an empty list
    assert deduplicate([]) == []
    
    # Negative numbers and zero
    assert deduplicate([0, -1, 0, -2, -1]) == [0, -1, -2]

    print("✅ All deduplicate tests passed!")


if __name__ == "__main__":
    test_char_frequency_suite()
    test_char_frequency_only_alpha_suite()
    test_deduplicate()