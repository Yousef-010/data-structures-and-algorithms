from hashmap.hashmap import HashTable
from Trees.Binary_tree import BinaryTree, Node


def tree_intersection(tree_one, tree_two):
    """
    For each node in tree_a traverse through tree_b, If node in tree_one == node in tree_two, add node.Value to common_values set .
    arguments: tree_one, tree_two
    return: common_values set.
    """
    hash_map = HashTable()
    common_values = set()

    values_of_tree_one = BinaryTree.pre_order(tree_one)
    values_of_tree_two = BinaryTree.pre_order(tree_two)

    for num in values_of_tree_one:
        hash_map.set(str(num), num)

    for num in values_of_tree_two:
        if hash_map.contains(str(num)):
            common_values.add(num)

    return sorted(common_values)