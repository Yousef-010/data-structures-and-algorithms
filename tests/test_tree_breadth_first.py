import pytest
from Trees.Binary_tree import BinaryTree, Node
from challengs.breadth_first_traversal.tree_breadth_first import *


def test_exists():
    assert breadth_first


def test_tree_empty():
    """
    test empty tree
    """
    actual = breadth_first(None)
    expected = []
    assert actual == expected


def test_one_node():
    """
    test tree with one node
    """
    tree = BinaryTree()
    tree.root = Node(2)
    expected = [2]
    actual = breadth_first(tree)
    assert actual == expected


def test_five_node():
    """
    test tree with one node
    """
    tree = BinaryTree()
    tree.root = Node(2)
    tree.root.left = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right = Node(6)
    expected = [2, 3, 6, 4, 5]
    actual = breadth_first(tree)
    assert actual == expected


def test_our_example(tree):
    """
    test our example in the code challenge requirement
    """
    actual = breadth_first(tree)
    expected = [2, 7, 5, 2, 6, 9, 5, 11, 4]
    assert actual == expected


###########
# fixture
###########
@pytest.fixture
def tree():
    tree = BinaryTree()
    tree.root = Node(2)
    tree.root.left = Node(7)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(6)
    tree.root.left.right.left = Node(5)
    tree.root.left.right.right = Node(11)
    tree.root.right = Node(5)
    tree.root.right.right = Node(9)
    tree.root.right.right.left = Node(4)
    return tree
