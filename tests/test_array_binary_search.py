import pytest
from array_binary_search.array_binary_search import sort_array, array_binary_search


def test_sort_array_base_case():
    """
        this function to test an array of integers and return the sorted array in the right case
    """
    actual = sort_array([4, 8, 15, 16, 23, 42])
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


def test_sort_array_empty_case():
    """
        this function to test an array of integers and return empty array in the wrong case
    """
    actual = sort_array([])
    expected = 'Invalid ARRAY SIZE ( EMPTY ARRAY )'
    assert actual == expected


def test_array_binary_search_Exist_case():
    """
    this function to test the base ( normal ) case and return 2
    """
    actual = array_binary_search([4, 8, 15, 16, 23, 42], 15)
    expected = 2
    assert actual == expected


def test_array_binary_search_four_case():
    """
    this function to test the [-131, -82, 0, 27, 42, 68, 179], 42 and return 4
    """
    actual = array_binary_search([-131, -82, 0, 27, 42, 68, 179], 42)
    expected = 4
    assert actual == expected


def test_array_binary_search_NotExist_case():
    """
    this function to test the base ( normal ) case and return -1
    """
    actual = array_binary_search([11, 22, 33, 44, 55, 66, 77], 90)
    expected = -1
    assert actual == expected


def test_array_binary_search_NotExist_four_case():
    """
    this function to test the [1, 2, 3, 5, 6, 7], 4 and return -1
    """
    actual = array_binary_search([1, 2, 3, 5, 6, 7], 4)
    expected = -1
    assert actual == expected


def test_array_binary_search_Empty_array_case():
    """
    this function to test the base ( normal ) case and return the same array ( empty array )
    """
    actual = array_binary_search([], 9)
    expected = 'Invalid ARRAY SIZE ( EMPTY ARRAY )'
    assert actual == expected
