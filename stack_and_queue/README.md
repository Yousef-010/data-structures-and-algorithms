# Stacks and Queues 

## Challenge
- Implement both a Stack and a Queue
- Add to stack:
  - push:
    - Arguments: value
    - adds a new node with that value to the top of the stack with an O(1) Time performance.

  - pop:
    - Arguments: none
    - Returns: the value from node from the top of the stack
    - Removes the node from the top of the stack
    - Should raise exception when called on empty stack

  - is_empty:
    - Arguments: none
    - Returns: Boolean indicating whether the stack is empty.

  - peek :
    - Arguments: none
    - Returns: Value of the node located at the top of the stack
    - Should raise exception when called on empty stack
  

- Add to queue:
  - enqueue:
    - Arguments: value
    - adds a new node with that value to the back of the queue with an O(1) Time performance.

  - dequeue:
    - Arguments: none
    - Returns: the value from node from the front of the queue
    - Removes the node from the front of the queue
    - Should raise exception when called on empty queue

  - is_empty:
    - Arguments: none
    - Returns: Boolean indicating whether the queue is empty
  - peek: 
    - Arguments: none
    - Returns: Value of the node located at the front of the queue
    - Should raise exception when called on empty queue

### Approach & Efficiency
- Stack and Queue Logic


- Big O for stack Implementation 
  - Time 
    - push 0(1)
    - pop 0(1)
    - is_empty O(1)
    - peek 0(1)
    - Dunder str O(n) n equal the length of the stack
  - Space : 
    - push 0(1)
    - pop 0(1)
    - is_empty O(1)
    - peek 0(1)


- Big O for queue Implementation 
  - Time 
    - enqueue 0(1)
    - dequeue 0(1)
    - is_empty O(1)
    - peek 0(1)
    - Dunder str O(n) n equal the length of the queue
  - Space : 
    - enqueue 0(1)
    - dequeue 0(1)
    - is_empty O(1)
    - peek 0(1)

#### API


- push : create new node with the value and make the next of the node equal the top and the top equal the node
- pop : check if the stack is empty, if yes raise error, if no top equal the next of the top 
- peek : check if the stack is empty, if yes raise error, if no return the top 
- is_empty : check if the top is None, if yes return True which is empty stack, if no return False which is not empty stack
- enqueue : create new node with the value and check if the queue is empty, if yes the front equal node and the rear equal node , if no the next of the rear equal node, and rear equal node
- dequeue : check if the queue is empty, if yes raise error, if no the front equal the next of the front 
- is_empty : check if the front is None, if yes return True which is empty queue, if no return False which is not empty queue
- peek :check if the queue is empty, if yes raise error, if no return the front


##### TEST 
- 16 test passed 
> pytest .\tests\test_stack_and_queue.py 
