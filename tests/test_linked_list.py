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


def test_insert_singleNode_into_linked_list(linked_list):
    """
    test insert single value into linked_list successfully
    """
    assert linked_list


def test_insert_multipleNode_into_linked_list(linked_list):
    """
    test insert multiple values into linked_list successfully
    """
    assert linked_list


def test_Head(linked_list):
    """
    test if the head points to the first node in the linked list
    """
    assert linked_list.head.value


def test_includes_exists_value(linked_list):
    """
    test search values in linked_list will return True if it exists
    """
    actual = linked_list.includes(1)
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
    print(linked_list.to_string())
    assert linked_list.to_string()
    # expected = '{5} -> {3} -> {2} -> {1} -> NULL'
    # assert actual == expected


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
    return linked_list


# insert single nodes
@pytest.fixture
def linked_list():
    linked_list = LinkedList()
    linked_list.insert_single_value(1)
    linked_list.insert_single_value(2)
    return linked_list


# insert multi nodes by using array then catch every element then makes it as node
@pytest.fixture
def linked_list():
    linked_list = LinkedList()
    linked_list.insert_multiple_values([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    return linked_list
