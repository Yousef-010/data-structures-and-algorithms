import pytest
from array_insert_shift.array_insert_shift import array_insert_shift


def test_array_insert_shift_even_array():
    actual = array_insert_shift([2, 4, 6, -8], 5)
    expected = [2, 4, 5, 6, -8]
    assert actual == expected


def test_array_insert_shift_odd_array():
    actual = array_insert_shift([42, 8, 15, 23, 42], 16)
    expected = [42, 8, 15, 16, 23, 42]
    assert actual == expected


def test_array_insert_shift_empty_array():
    actual = array_insert_shift([], 16)
    expected = [16]
    assert actual == expected

