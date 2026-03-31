from word_count_file import count_words_in_file
from safe_int_parser import safe_parse_int


def test_count_words_in_file_basic(tmp_path):
	file_path = tmp_path / "sample.txt"
	file_path.write_text("Hello world hello", encoding="utf-8")

	result = count_words_in_file(str(file_path))
	assert result == {"hello": 2, "world": 1}


def test_count_words_in_file_with_punctuation(tmp_path):
	file_path = tmp_path / "sample2.txt"
	file_path.write_text("Hi, hi. HI!", encoding="utf-8")

	result = count_words_in_file(str(file_path))
	assert result == {"hi": 3}


def test_count_words_in_file_not_found_returns_empty_dict():
	result = count_words_in_file("no_such_file_12345.txt")
	assert result == {}


def test_safe_parse_int_valid_value():
	assert safe_parse_int("42") == 42


def test_safe_parse_int_invalid_value_returns_zero():
	assert safe_parse_int("abc") == 0


def test_safe_parse_int_clamps_to_max():
	assert safe_parse_int("100", max_value=50) == 50


def test_safe_parse_int_clamps_to_min():
	assert safe_parse_int("-10", min_value=0) == 0
