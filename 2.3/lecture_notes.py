

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


class StackDeque:
    def __init__(self, data=deque()):
        self.data = data

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()


my_deque = StackDeque()
my_deque.push(1)
my_deque.push(2)
my_deque.push(3)
my_deque.push(4)
my_deque.push(5)

print(my_deque.data)
print(my_deque.pop())
print(my_deque.data)


"""
Exercise 1: "155. MinStack" (https://leetcode.com/problems/min-stack/)

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
    MinStack() initializes the stack object.
    void push(val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.
 

* Example:

    Input:
        ["MinStack","push","push","push","getMin","pop","top","getMin"]
        [[],[-2],[0],[-3],[],[],[],[]]

    Output:
        [null,null,null,null,-3,null,0,-2]

    Explanation:
        MinStack minStack = new MinStack();
        minStack.push(-2);
        minStack.push(0);
        minStack.push(-3);
        minStack.getMin(); // return -3
        minStack.pop();
        minStack.top();    // return 0
        minStack.getMin(); // return -2
"""

class MinStack:

    def __init__(self, data=deque()):
        self.data = data



# since min element needs to be retrieved in constant time, always append min to right
# before adding to stack see if the new element is less than the current min, if so pushLeft, else push 