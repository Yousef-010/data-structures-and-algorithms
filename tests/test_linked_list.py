import pytest
from linked_list.linked_list import LinkedList, Node


def test_Nodes(node):
    """
    test if the Node created successfully
    """
    assert node


def test_empty_linked_list_creation(linked_list):
    """
    test successfully instantiate an empty linked list
    """
    assert linked_list


def test_insert__SingleNodes_into_linked_list(linked_list):
    """
    test insert single value into linked_list successfully
    """
    linked_list.insert(1)
    assert linked_list


def test_insert__multipleNodes_into_linked_list(linked_list):
    """
    test insert single value into linked_list successfully
    """

    linked_list.insert(4)
    linked_list.insert(5)
    linked_list.insert(6)
    assert linked_list


def test_Head(linked_list):
    """
    test if the head points to the first node in the linked list
    """
    linked_list.insert(7)
    actual = linked_list.head.value
    expected = 7
    assert actual == expected
    # assert linked_list.head.value


def test_includes_exists_value(linked_list):
    """
    test search values in linked_list will return True if it exists
    """
    actual = linked_list.includes(2)
    expected = True
    assert actual == expected


def test_includes_Not_exists_value(linked_list):
    """
    test search values in linked_list will return False if it does not exist
    """
    actual = linked_list.includes(100)
    expected = False
    assert actual == expected


def test_to_string(linked_list):
    """
    test represent the linked list values in a formatted way
    """
    assert linked_list.to_string()











##############
# pytest.fixture
##############

# create Node
@pytest.fixture
def node():
    node = Node(5)
    return node


# create linked_list
@pytest.fixture
def linked_list():
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    return linked_list



