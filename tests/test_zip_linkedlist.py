import pytest

from challengs.linkedList_zip.linkedlist_zip import zip_lists
from linked_list.linked_list import LinkedList, Node


def test_zip_linked_lists_if_both_linked_lists_is_empty():
    # EMPTY linked list
    first_linked_list = LinkedList()
    # EMPTY linked list
    second_linked_list = LinkedList()
    actual = zip_lists(first_linked_list, second_linked_list)
    expected = 'your linked_lists id empty'
    assert actual == expected


def test_zip_linked_lists_if_first_linked_list_is_empty():
    # EMPTY linked list
    first_linked_list = LinkedList()
    # NOT EMPTY linked list
    second_linked_list = LinkedList()
    second_linked_list.append(1)
    actual = zip_lists(first_linked_list, second_linked_list).to_string()
    expected = second_linked_list.to_string()
    assert actual == expected


def test_zip_linked_lists_if_second_linked_list_is_empty():
    # NOT EMPTY linked list
    first_linked_list = LinkedList()
    first_linked_list.append(1)
    # EMPTY linked list
    second_linked_list = LinkedList()
    actual = zip_lists(first_linked_list, second_linked_list).to_string()
    expected = first_linked_list.to_string()
    assert actual == expected


def test_zip_two_equal_length_linked_list(first_linked_list, second_linked_list):
    """
    this is for test zipping with two equals length of linked list
    """
    first_linked_list.append(2)
    second_linked_list.append(4)
    actual = zip_lists(first_linked_list, second_linked_list).to_string()
    expected = '{1} -> {5} -> {3} -> {9} -> {2} -> {4} -> NULL'
    assert actual == expected


def test_zip_linked_list_first_grater_than_second(first_linked_list, second_linked_list):
    """
    this is for test zipping with the first linked list is greater than the second_linked_list.
    """
    first_linked_list.append(2)
    actual = zip_lists(first_linked_list, second_linked_list).to_string()
    expected = '{1} -> {5} -> {3} -> {9} -> {2} -> NULL'
    assert actual == expected


def test_zip_linked_list_second_grater_than_first(first_linked_list, second_linked_list):
    """
        this is for test zipping with the second linked list is greater than the first linked list
    """
    second_linked_list.append(4)
    actual = zip_lists(first_linked_list, second_linked_list).to_string()
    expected = '{1} -> {5} -> {3} -> {9} -> {4} -> NULL'
    assert actual == expected


#############
# fixtures
#############

@pytest.fixture
def first_linked_list():
    first_linked_list = LinkedList()
    first_linked_list.append(1)
    first_linked_list.append(3)
    return first_linked_list


@pytest.fixture
def second_linked_list():
    second_linked_list = LinkedList()
    second_linked_list.append(5)
    second_linked_list.append(9)
    return second_linked_list
