import pytest
from fastapi.testclient import TestClient

from fastapi_app import app
from iterators_generators import RunningSum, even_number_generator, safe_int_parse
from timed_problems import first_non_repeating_char, merge_sorted


def test_even_generator_basic():
    result = list(even_number_generator(3, 11))
    assert result == [4, 6, 8, 10]


def test_even_generator_single():
    result = list(even_number_generator(2, 2))
    assert result == [2]


def test_even_generator_empty():
    result = list(even_number_generator(9, 7))
    assert result == []


def test_running_sum_basic():
    running_sum = RunningSum([1, 2, 3, 4])
    assert list(running_sum) == [1, 3, 6, 10]


def test_running_sum_empty():
    running_sum = RunningSum([])
    assert list(running_sum) == []


def test_safe_int_parse_basic():
    result = safe_int_parse(["10", "x", "-3", "7.5", "0"])
    assert result == [10, -3, 0]


def test_first_non_repeating_basic():
    assert first_non_repeating_char("leetcode") == "l"


def test_first_non_repeating_none():
    assert first_non_repeating_char("aabb") == ""


def test_first_non_repeating_swiss():
    assert first_non_repeating_char("swiss") == "w"


def test_merge_sorted_basic():
    result = merge_sorted([1, 3, 5], [2, 4, 6])
    assert result == [1, 2, 3, 4, 5, 6]


def test_merge_sorted_with_empty():
    result = merge_sorted([], [1, 2])
    assert result == [1, 2]


def test_merge_sorted_duplicates():
    result = merge_sorted([1, 1, 2], [1, 3])
    assert result == [1, 1, 1, 2, 3]


def test_merge_sorted_invalid_type():
    with pytest.raises(TypeError):
        merge_sorted("abc", [1, 2])


def test_home_route():
    client = TestClient(app)
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Day 6!"}


def test_first_non_repeating_endpoint_success():
    client = TestClient(app)
    response = client.post("/first-non-repeating", json={"text": "swiss"})

    assert response.status_code == 200
    assert response.json() == {"result": "w"}


def test_first_non_repeating_endpoint_empty_result():
    client = TestClient(app)
    response = client.post("/first-non-repeating", json={"text": "aabb"})

    assert response.status_code == 200
    assert response.json() == {"result": ""}


def test_first_non_repeating_endpoint_invalid_type():
    client = TestClient(app)
    response = client.post("/first-non-repeating", json={"text": 123})

    assert response.status_code == 422
