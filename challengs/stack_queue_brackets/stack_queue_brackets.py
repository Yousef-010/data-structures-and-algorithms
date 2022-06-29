from stack_and_queue.stack_and_queue import *


def validate_brackets(string):
    pairings = {'(': ')', '{': '}', '[': ']'}
    stack = Stack()

    for s in string:
        if s not in pairings and s not in pairings.values():
            continue

        if s in pairings:
            stack.push(s)
            continue

        try:
            the_top = stack.pop()
        except EmptyStackException:
            return False

        if s != pairings[the_top]:
            return False

    return stack.is_empty()



