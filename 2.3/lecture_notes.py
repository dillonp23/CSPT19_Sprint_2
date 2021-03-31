

"""
Sprint 2.3 Lecture Notes: Stacks & Queues


* Stacks:
    - LIFO
    - Built on either a Dynamic Array (List in Python) or LinkedList data structure
    
    Operations:

        * Adding to stack: "def push(item)"
            - adds new value to top
            - takes a single item as an argument
            - returns nothing

        * Removing from stack: "def pop()"
            - takes no arguments
            - removes/returns top-most value of Stack 

    
    Time & Space Complexity of hypethetical operations on a Stack built with a dynamic array (List):

        * Accessing a item on bottom of list
            - O(n) linear

        * Search for an item
            - O(n)

        Insertion/Deletion (when not at end)
            - O(n) based on the underlying List data type



    Time & Space Complexity of hypethetical operations on a Stack built with a LinkedList:

        * Accessing a item on bottom of list
            - O(n) linear

        * Search for an item
            - O(n)

        Insertion/Deletion (when not at end)
            - O(1) based on the underlying LinkedList data type


    
* Python deque ("Deck") types
    - can be used to build our stacks/queues
    - a double ended queue in Python that acts as a stack/queue
    - offers O(1) appends/pops to both ends of data structure

    - 4 different operations:
        - popLeft()
        - appendLeft(item)
        - pop()
        - append(item)
"""

from collections import deque

my_deck = deque()

my_deck.append('a')
my_deck.append('b')
my_deck.append('c')
my_deck.append('c')

print(my_deck.count('c'))

