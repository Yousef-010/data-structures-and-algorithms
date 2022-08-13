import pytest
from challengs.tree_intersection.tree_intersection import tree_intersection
from Trees.Binary_tree import Node, BinaryTree


def test_exits():
    assert tree_intersection


def test_return_common_values(tree_one, tree_two):
    actual = tree_intersection(tree_one, tree_two)
    expected = [100, 125, 160, 175, 200, 350, 500]
    assert actual == expected


@pytest.fixture
def tree_one():
    tree_one = BinaryTree()
    tree_one.root = Node(150)
    tree_one.root.left = Node(100)
    tree_one.root.right = Node(250)
    tree_one.root.left.left = Node(75)
    tree_one.root.left.right = Node(160)
    tree_one.root.left.right.left = Node(125)
    tree_one.root.left.right.right = Node(175)
    tree_one.root.right.left = Node(200)
    tree_one.root.right.right = Node(350)
    tree_one.root.right.right.left = Node(300)
    tree_one.root.right.right.right = Node(500)
    return tree_one


@pytest.fixture
def tree_two():
    tree_two = BinaryTree()
    tree_two.root = Node(42)
    tree_two.root.left = Node(100)
    tree_two.root.right = Node(600)
    tree_two.root.left.left = Node(15)
    tree_two.root.left.right = Node(160)
    tree_two.root.left.right.left = Node(125)
    tree_two.root.left.right.right = Node(175)
    tree_two.root.right.left = Node(200)
    tree_two.root.right.right = Node(350)
    tree_two.root.right.right.left = Node(4)
    tree_two.root.right.right.right = Node(500)
    return tree_two
