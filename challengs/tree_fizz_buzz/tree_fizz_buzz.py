from stack_and_queue.stack_and_queue import *
from Trees.karyTree import *


def fizz_buzz_tree(tree):
    def _fizz_buzz(value):
        value = int(value)
        if value % 3 == 0 and value % 5 == 0:
            return "FizzBuzz"
        elif value % 3 == 0:
            return "Fizz"
        elif value % 5 == 0:
            return "Buzz"
        else:
            return str(value)

    f_b_queue = Queue()
    output = []
    fizz_tree = KaryTree(tree.root)
    f_b_queue.enqueue(fizz_tree.root)
    while not f_b_queue.is_empty():
        cur_node = f_b_queue.dequeue()
        new_node = _fizz_buzz(cur_node.value)
        output.append(new_node)
        for child in cur_node.children:
            f_b_queue.enqueue(child)

    return output
