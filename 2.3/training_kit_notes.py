
"""
Sprint 2 - Module 3: Stack & Queues


* Objective 1: Queues
    - FIFO (First-in, First-out)
    - Analogous to a line or queue in real life

    
    Time Complexity:

        * Enqueue: O(1) - constant time
            - adds item to back of queue

        * Dequeue: O(1) - constant time
            - remove item from front of queue

        * Peek: O(1) - constant time
            - inspect item at front of queue without removing

    
    Space Complexity:

        * O(n) - linear space
            - each item in queue will take up space in memory

    
    Strengths:
        - primary strength is that all of its operations are fast O(1) - constant

    
    Weaknesses:
        - there are no specific weaknesses with queues
        - very targeted data structure designed to do only a few things well


    When to use queues?
        - useful in instances where you need FIFO order of operations
        - example use cases:
            
            * Web server
                - process and respond to requests in order received
            
            * Breadth-first traversal
                - a method of traversing heirachical data structures
                - queues can be used to facillitate this type of traversal



* Objective 2: Stacks
    - LIFO (last-in, first-out order)
    - like a stack of papers
        - last paper added to stack will be first removed

    
    Time Complexity:

        * Push: O(1) - constant time
            - adding to top of stack

        * Pop: O(1) - constant time
            - removing item from top of stack

        * Peek: O(1) - constant time
            - inspect top item of stack without removing


    Space Complexity:

        * O(n) - linear space


    Strengths:
        - primary strength is fast operations, all O(1) constant

    
    Weaknesses:
        - no specific weaknesses as its a very targeted data structure


    When to use a stack?
        - useful in any situation where LIFO order is needed
        - example use cases:

            * Parsing strings
                - ensuring all parentheses of a string are balanced

            * Function calls and executions
                - managed on a call stack
                - when calling a function, its added to the call stack
                - when finished executing a function its removed from call stack

            * Iterative depth-first search
                - traversing down the length of a data structure
                - if result isn't found, will pop back to the location at which it branched 
"""



"""
* Objective 3: Implementing a Queue using a Linked List
"""

class LinkedListNode:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
    
    def __repr__(self):
        return f"Node({self.value})->{self.next}"


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None


    def enqueue(self, item):
        new_node = LinkedListNode(item)

        #  check if queue empty
        if self.isEmpty():
            self.front = new_node
            self.rear = new_node
        
        else:
            # add new node to rear
            self.rear.next = new_node
            # reassign rear to new node
            self.rear = new_node


    def dequeue(self):
        # check if queue is empty
        if self.isEmpty():
            return

        # keep copy of previous front
        old_front = self.front
        # set new front
        self.front = old_front.next

        #  check if queue is now empty
        if self.front is None:
            # update rear to none
            self.rear = None

        return old_front


    def isEmpty(self):
        return self.front == None