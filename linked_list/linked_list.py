
class Node:
    """
    It will store the data and the reference to the next node
    """
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """
    create a sequence of Nodes
    """
    def __init__(self):
        self.head = None

    def insert(self, value):
        """
        insert value into LinkedList as node
        """
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            self.head = node
            self.head.next = current

    def includes(self, key):
        search_element = Node(key)
        current = self.head
        while current:
            if current.value == search_element.value:
                return True
            current = current.next
        return False

    def to_string(self):
        """
        to  represent all the values in the Linked List, formatted
        """
        current = self.head
        formatting = ''
        opening = '{'
        closing = '}'
        while current:
            formatting += f'{opening}{current.value}{closing} -> '
            current = current.next
        formatting += 'NULL'
        return formatting
