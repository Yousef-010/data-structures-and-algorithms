# Trees
- Node
  - Create a Node class that has properties for the value stored in the node
  - the left child node, and the right child node.
- Binary Tree
  - Create a Binary Tree class
  - Define a method for each of the depth first traversals:
    - pre order
    - in order
    - post order which returns an array of the values, ordered appropriately.
    - findMax :
      - argument : None
      - return the maximum value in a tree
- Binary Search Tree
  - Create a Binary Search Tree class
    -This class should be a subclass (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
  - Add
    - Arguments: value
    - Return: nothing
    - Adds a new node with that value in the correct location in the binary search tree.
  - Contains
    - Argument: value
    -Returns: boolean indicating whether the value is in the tree at least once.


## Challenge
- Create a Binary Tree class with these methods :
  - pre-order 
  - in-order 
  - post-order 
- Create a subclass form binary Tree class called BinarySearchTree with these methods:
  - add : add node into tree maybe in the left or in the right 
  - contain : return true if the tree contain the value , False if the tree does not contain

### Approach & Efficiency
- in the pre-order , in-order and post-order i used the recursive function to traverse through the 
- tree nodes and takes the preferred node into list 
- after the end of the tree return the list 
- 
- Big o notation : 
  - Time complexity :
    - pre-order : o(n)
    - in-order : o(n)
    - post-order : o(n)
    - add : O(log2n)
    - contain : O(log2n)
    - findMax : O(n)
  - space complexity : 
    - pre-order : o(n)
    - in-order : o(n)
    - post-order : o(n)
    - add : O(1)
    - contain : O(1)
    - findMax : O(n)
#### API

- add method : 
  - check if the root is none if yes 
  - create a new node with the value 
  - declare var called cur_node with the value of the root as initial value
  - using while loop 
  - check if the valus that i have to add is greater than the root value then add it into the right 
  - if it is less than the root add into left 
  - repeat the Process to add the elements that you want 
- contain method : 
  - declare boolean variable to store the result 
  - declare var called cur_node with the value of the root as initial value
  - using while loop 
  - check if the value is greate than the root that mean we need to ignore the left part
  - check if the value is less than the root that mean we need to ignore the right part
  - and repeat the process until finding the value 
  - return True if the value is in tree 
  - return False if the value is not in tree
- findMax method : 
  - in this method i 
  - check if the tree is empty return none 
  - declare a function with root value and the max with zero
  - check if the root is less than the max , if yes max will equal the value of the root
  - else do the function again ( recursive function ) with the left node of the root 
  - else do the function again ( recursive function ) with the right node of the root
  - return the maximum value 
  - return the recursive function with the root node of the tree

##### Test 
- All tests passed
- pytest .\tests\test_binary_tree.py    
- pytest .\tests\test_binary_search_tree.py



> whiteboard images : 
> 
![find_max image](code%20challenge%2017%20.png)