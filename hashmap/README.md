# Hash map 

> Hashtable
- is a data structure that implements a set abstract data type, a structure that can map keys to values



> Challenge
- Implement a Hashtable Class with the following methods:
  - set
    - Arguments: key, value
    - Returns: nothing
    - This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
    - Should a given key already exist, replace its value from the value argument given to this method.
  - get
    - Arguments: key
    - Returns: Value associated with that key in the table
  - contains
    - Arguments: key
    - Returns: Boolean, indicating if the key exists in the table already.
  - keys
    - Returns: Collection of keys
  - hash
    - Arguments: key
    - Returns: Index in the collection for that key


> Approach & Efficiency
- Big O notation for all methods

  - contains:
    - Time Complexity: O(n)
    - Space Complexity: O(n) 

  - keys:
    - Time Complexity: O(1)
    - Space Complexity: O(1)

  - hash:
    - Time Complexity: O(1)
    - Space Complexity: O(1)

  - set:
    - Time Complexity: O(1)
    - Space Complexity: O(n)  

  - get:
    - Time Complexity: O(n)
    - Space Complexity: O(n)  



> TEST 
- all tests passed 
- run `pytest .\tests\test_hashmap.py`