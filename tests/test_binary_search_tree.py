import pytest
from Trees.Binary_search_tree import *


def test_exists():
    assert BinarySearchTree


def test_instantiate_empty():
    """
    instantiate BinarySearchTree instances
    """
    tree = BinarySearchTree()
    actual = tree.root
    expected = None
    assert actual == expected


def test_add_to_empty():
    """
    add node to empty tree
    """
    tree = BinarySearchTree()
    tree.add(10)
    actual = tree.root.value
    expected = 10
    assert actual == expected


def test_add_left():
    """
    can successfully add a left child
    """
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    actual = tree.root.left.value
    expected = 5
    assert actual == expected


def test_add_right():
    """
     can successfully add a right child
    """
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(15)
    actual = tree.root.right.value
    expected = 15
    assert actual == expected


def test_add_in_deep_right(tree):
    """
     can successfully add in deep right child
    """
    tree.add(30)
    actual = tree.root.right.right.value
    expected = 30
    assert actual == expected


def test_add_in_deep_left(tree):
    """
    can successfully add in deep left child
    """
    tree.add(1)
    actual = tree.root.left.left.left.value
    expected = 1
    assert actual == expected


def test_contains(tree):
    """
    Returns True if the value exists in the tree
    """
    actual = tree.contains(3)
    expected = True
    assert actual == expected


def test_not_contains(tree):
    """
    Returns False if the value not exists in the tree
    """
    actual = tree.contains(100)
    expected = False
    assert actual == expected


###########
# fixture
###########
@pytest.fixture
def tree():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    tree.add(3)
    return tree
