import pytest
from challengs.tree_fizz_buzz.tree_fizz_buzz import *
from Trees.karyTree import *


def test_exists():
    assert fizz_buzz_tree


def test_empty():
    """
    test empty tree
    """
    tree = KaryTree()
    actual = tree.breadth_first()
    expected = 'empty tree'
    assert actual == expected


def test_original_tree(tree):
    """
    test the original tree using breadth first traversal
    return array of nodes
    """
    fizz_buzz_tree(tree)
    actual = tree.breadth_first()
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    assert actual == expected


def test_from_one_to_fifteen(tree):
    """
    test this tree as an example

                            1
                2                       3
            4  5  6               7     8          9
        10  11 12              13            14   15

    return the same tree but replace the value of node with the correct string
    """
    actual = fizz_buzz_tree(tree)
    expected = ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
    assert actual == expected



###########
# fixture
###########
@pytest.fixture
def tree():
    first_node = Node(1)
    second_node = Node(2)
    third_node = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)
    eight = Node(8)
    nine = Node(9)
    ten = Node(10)
    eleven = Node(11)
    twelve = Node(12)
    thirteen = Node(13)
    fourteen = Node(14)
    fifteen = Node(15)

    first_node.children = [second_node, third_node]
    second_node.children = [four, five, six]
    third_node.children = [seven, eight, nine]
    four.children = [ten]
    five.children = [eleven]
    six.children = [twelve]
    seven.children = [thirteen]
    nine.children = [fourteen, fifteen]

    return KaryTree(first_node)
