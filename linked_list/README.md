> ### Singly Linked List
A Linked List is a data structure represent the data as nodes each node contain
 - The value 
 - The pointer to the next node 

> #### Challenge
 - Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
 - Create a Linked List class
 - create these methods in the linked list 
   - insert
     - Arguments: value
     - Returns: nothing
       - Adds a new node with that value to the head of the list with an O(1) Time performance. 
   - includes
     - Arguments: value
     - Returns: Boolean
       - Indicates whether that value exists as a Node’s value somewhere within the list.
   - to string
     - Arguments: none
     - Returns: a string representing all the values in the Linked List, formatted as:
       - "{ a } -> { b } -> { c } -> NULL"

> ##### Approach & Efficiency
 - What approach did you take? why? 
    - Single Linked List
 - What is the Big O space/time for this approach?
     - insertion time complexity : BigO = O(1)
       - insertion space complexity : BigO = O(n)
     - includes time complexity : BigO = O(n)
       - includes space complexity : BigO = O(1)
     - to_string time complexity : BigO = O(n)
       - to_string space complexity : BigO = O(1)


> ##### API 
    - Insert
        - it is a method take a value as a parameter and make a new node with the 
          same value, then inert the new node into linkedList 
    - Include
        - it is a method take a value as a parameter and search for it in the 
          linkedList and return True if the value exist in the linked list, if not 
          return False 
    - to_string
        - it is a method to represent the collection of the values inside linkedList
          and return it in a spicific foramtted way 