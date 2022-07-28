import pytest
from sorting.Quick.quick_sort import *


def test_empty_array():
    """
    this function test an empty array ( the length of the array equals zero )
    """
    arr = []
    actual = quick_sort(arr,  0, len(arr)-1)
    expected = 'EMPTY ARRAY'
    assert actual == expected


def test_len_equal_one():
    """
    this function test an array of length equal one
    """
    arr = [1]
    actual = quick_sort(arr,  0, len(arr)-1)
    expected = [1]
    assert actual == expected


def test_random_array():
    """
    this function test an array of random array
    """
    arr = [8, 4, 23, 42, 16, 15]
    actual = quick_sort(arr, 0, len(arr)-1)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


def test_reverse_sorted_array():
    """
    this function test reverse sorted array
    """
    arr = [20, 18, 12, 8, 5, -2]
    actual = quick_sort(arr,  0, len(arr)-1)
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected


def test_few_uniques_array():
    """
    this function test an array of uniques number
    """
    arr = [5, 12, 7, 5, 5, 7]
    actual = quick_sort(arr,  0, len(arr)-1)
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected


def test_nearly_sorted_array():
    """
    this function test an array of nearly sorted array
    """
    arr = [2, 3, 5, 7, 13, 11]
    actual = quick_sort(arr,  0, len(arr)-1)
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected
