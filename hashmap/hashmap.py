class Node:
    """
    this class used to instantiate node with 2 attributes: the value and the next pointer
    """
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """
    this class used to instantiate a linked list with head attribute
    """
    def __init__(self):
        self.head = None

    def insert(self, value):
        """
        this method used to insert node with its value into linked list
        """
        node = Node(value)
        node.next = self.head
        self.head = node


class HashTable:
    """
    this class used to instantiate a hash table as a data structure to store data in key value pairs
    """
    def __init__(self, size = 1024):
        self.size = size
        self.__buckets = [None] * size
        self.__keys_arr = []

    def __hash(self, key):
        """
        this method used to hash a key
        parameter: key
        return: hashed key
        """
        return sum([ord(element) for element in key]) * 283 % self.size

    def set(self, key, value):
        """
        this method used to set a pair (hashed key , value ) into a hash table
        """
        hashed_key = self.__hash(key)
        if self.__buckets[hashed_key] is None:
            linked_list = LinkedList()
            self.__buckets[hashed_key] = linked_list
        self.__keys_arr.append(key)
        self.__buckets[hashed_key].insert((key, value))

    def get(self, key):
        """
        this method used to find the value based on a specific key form the hash table
        """
        hash_key = self.__hash(key)
        linked_list = self.__buckets[hash_key]
        current = linked_list.head
        while current:
            if current.value[0] == key:
                return current.value[1]
            current = current.next
        return None

    def contains(self, key):
        """
        this method used to return True if the key exists in the hash table, and False if it does not
        """
        hash_key = self.__hash(key)
        linked_list = self.__buckets[hash_key]
        if not linked_list:
            return False
        current = linked_list.head
        while current:
            if current.value[0] == key:
                return True
            current = current.next
        return False

    def keys(self):
        """
        this method used to get all the keys in the hash table and stor them in keys_arr
        """
        return self.__keys_arr


if __name__ == '__main__':
    hash_map = HashTable()
    hash_map.set('key_1', 'yousef')
    hash_map.set('key_2', 'ahmad')
    hash_map.set('key_3', 'mohammad')

    print(hash_map.contains('key_1'))
    print(hash_map.contains('key_5'))

    print(hash_map.keys())

    print(hash_map.get('key_5'))
