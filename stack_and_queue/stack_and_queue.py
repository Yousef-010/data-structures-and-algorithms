class EmptyStackException(Exception):
    pass


class EmptyQueueException(Exception):
    pass


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        """
        Arguments: value
        return : adds a new node with that value to the top of the stack with an O(1) Time performance.
        """
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        """
        Arguments: none
        Returns: the value from node from the top of the stack
        Removes the node from the top of the stack
        Should raise exception when called on empty stack
        """
        if self.is_empty():
            raise EmptyStackException('THIS STACK IS EMPTY')
        else:
            pooped = self.top
            self.top = self.top.next
        return pooped.value

    def is_empty(self):
        """
        Arguments: none
        Returns: True if the stack is empty and False if the stack is not empty.
        """
        return True if self.top is None else False

    def peek(self):
        """
        Arguments: none
        Returns: Value of the node located at the top of the stack
        Should raise exception when called on empty stack
        """
        if self.is_empty():
            raise EmptyStackException('THIS STACK IS EMPTY')
        else:
            return self.top.value

    def __str__(self):
        current = self.top
        result = ''
        while current:
            result += str(current.value) + '\n'
            current = current.next
        return result


###########################################################


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        """
        Arguments: value
        adds a new node with that value to the back of the queue with an O(1) Time performance.
        """
        node = Node(value)
        if self.is_empty():
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        """
        Arguments: none
        Returns:the value from node from the front of the queue
        Removes the node from the front of the queue
        Should raise exception when called on empty queue
        """
        if self.is_empty():
            raise EmptyQueueException('THIS QUEUE IS EMPTY')
        else:
            dequeued = self.front
            self.front = self.front.next
        return dequeued.value

    def is_empty(self):
        """
        Arguments: none
        Returns: True if the stack is empty and False if the stack is not empty.
        """
        return True if self.front is None else False

    def peek(self):
        """
        Arguments: none
        Returns: Value of the node located at the front of the queue
        Should raise exception when called on empty stack
        """
        if self.is_empty():
            raise EmptyQueueException('THIS QUEUE IS EMPTY')
        else:
            return self.front.value

    def __str__(self):
        current = self.front
        result = ''
        while current:
            result += str(current.value) + '\t'
            current = current.next
        return result


###########################################################


if __name__ == '__main__':

    print('################################')
    print('________    Stack     ________')

    stack = Stack()
    stack.push(0)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    print(stack)

    print('THE TOP →', stack.top.value)
    print('TEH POPPED VALUE →', stack.pop())
    print('THE TOP AFTER POP →', stack.top.value)
    print('THIS PEEK →', stack.peek())
    print('IS EMPTY →', stack.is_empty())

    print('################################')
    print('________    Queue     __________')

    queue = Queue()
    queue.enqueue(0)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    print(queue)

    print('THE FRONT →', queue.front.value)
    print('THE REAR →', queue.rear.value)
    queue.enqueue(5)
    print('THE REAR AFTER ENQUEUE →', queue.rear.value)
    print('TEH DEQUEUED VALUE →', queue.dequeue())
    print('THE FRONT AFTER DEQUEUED →', queue.front.value)
    print('THIS PEEK →', queue.peek())
    print('IS EMPTY →', queue.is_empty())
