from stack_and_queue.stack_and_queue import *


class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinaryTree:
    """
    Define a method for each type of the Depth-first-Tree
    """
    def __init__(self):
        self.root = None

    def pre_order(self):
        """
        get the nodes from tree in depth-first root-left-right
        """
        if not self.root:
            return self.root

        def traverse(node, current_list):
            """
            store the value of nodes recursively
            """
            if node:
                current_list.append(node.value)
                if node.left is not None:
                    traverse(node.left, current_list)
                if node.right is not None:
                    traverse(node.right, current_list)
            return current_list

        pre_order_list = []
        traverse(self.root, pre_order_list)
        return pre_order_list

    def in_order(self):
        """
        get the nodes from tree in depth-first left-root-right
        """
        if not self.root:
            return self.root

        def traverse(node, current_list):
            """
            store the value of nodes recursively
            """
            if node.left is not None:
                traverse(node.left, current_list)
            current_list.append(node.value)
            if node.right is not None:
                traverse(node.right, current_list)
            return current_list

        in_order_list = []
        traverse(self.root, in_order_list)
        return in_order_list

    def post_order(self):
        """
        get the nodes from tree in depth-first left-right-root
        """
        def traverse(node, current_list):
            """
            store the value of nodes recursively
            """
            if node.left is not None:
                traverse(node.left, current_list)
            if node.right is not None:
                traverse(node.right, current_list)
            current_list.append(node.value)
            return current_list

        post_order_list = []
        traverse(self.root, post_order_list)
        return post_order_list

    def find_max(self):
        if self.root is None:
            return None

        def traverse(root, maximum=0):
            if root is None:
                return maximum
            if maximum < root.value:
                maximum = root.value
            left_of_tree = traverse(root.left, maximum)
            if maximum < left_of_tree:
                maximum = left_of_tree
            right_of_tree = traverse(root.right, maximum)
            if maximum < right_of_tree:
                maximum = right_of_tree
            return maximum
        return traverse(self.root)

    def __str__(self):
        if self.root is None:
            return 'None'
        else:
            res_list = self.pre_order()
            output = ''
            for i in res_list:
                output += f'{i}'
            return output


if __name__ == '__main__':
    t = BinaryTree()
    t.root = Node(10)
    t.root.left = Node(5)
    t.root.right = Node(15)
    t.root.left.left = Node(1)
    t.root.right.right = Node(20)

    print(t.pre_order())
    print(t.in_order())
    print(t.post_order())
    print(t.find_max())
