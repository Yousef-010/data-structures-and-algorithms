import pytest
from Trees.Binary_tree import *


def test_exists():
    assert Node


def test_create_node():
    """
    check if the node is created and it's pointers
    """
    node = Node(100)
    assert node
    assert node.left is None
    assert node.right is None


def test_tree_exists():
    """
    Can successfully instantiate a tree with a single root node
    """
    tree = BinaryTree()
    tree.root = Node(50)
    actual = tree.root.left
    expected = None
    actual2 = tree.root.right
    expected2 = None


def test_tree_root_exists():
    """
    Can successfully instantiate an empty tree
    """
    tree = BinaryTree()
    actual = tree.root
    expected = None
    assert actual == expected


def test_post_order(tree):
    """
    Can successfully return a collection from a postorder traversal
    """
    actual = tree.post_order()   # left, right, root
    expected = [1, 20, 5, 15, 10]
    assert actual == expected


def test_pre_order(tree):
    """
    Can successfully return a collection from a preorder traversal
    """
    actual = tree.pre_order()   # root,left, right
    expected = [10, 5, 1, 20, 15]
    assert actual == expected


def test_in_order(tree):
    """
    Can successfully return a collection from an inorder traversal
    """
    actual = tree.in_order()
    expected = [1, 5, 20, 10, 15]  # left, root, right
    assert actual == expected


def test_find_max_in_tree(tree2):
    """
    this test for finding the max value in a tree
    """
    actual = tree2.find_max()
    expected = 11
    assert actual == expected


def test_find_max_in_tree_two(tree2):
    """
    this test for finding the max value in a tree
    """
    tree2.root.right.right.right = Node(100)
    actual = tree2.find_max()
    expected = 100
    assert actual == expected



############
# fixture
############
@pytest.fixture
def tree():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(5)
    tree.root.right = Node(15)
    tree.root.left.left = Node(1)
    tree.root.left.right = Node(20)
    return tree


@pytest.fixture
def tree2():
    tree2 = BinaryTree()
    tree2.root = Node(2)
    tree2.root.left = Node(7)
    tree2.root.left.left = Node(2)
    tree2.root.left.right = Node(6)
    tree2.root.left.right.left = Node(5)
    tree2.root.left.right.right = Node(11)
    tree2.root.right = Node(5)
    tree2.root.right.right = Node(9)
    tree2.root.right.right.left = Node(4)
    return tree2

