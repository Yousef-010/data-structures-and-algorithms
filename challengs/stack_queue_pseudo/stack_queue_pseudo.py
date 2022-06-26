from stack_and_queue.stack_and_queue import Stack


class PseudoQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        self.stack1.push(value)

    def dequeue(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                data_moved = self.stack1.pop()
                self.stack2.push(data_moved)
        return self.stack2.pop()

    def __str__(self):
        result = ''
        current = self.stack1.top
        while current:
            result += '[' + str(current.value) + ']' + '->'
            current = current.next

        return result


if __name__ == "__main__":
    pq = PseudoQueue()
    pq.enqueue(20)
    pq.enqueue(15)
    pq.enqueue(10)
    pq.enqueue(5)
    print(pq)


