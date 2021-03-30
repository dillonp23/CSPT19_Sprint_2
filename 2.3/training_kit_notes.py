
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
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def __repr__(self):
        return f"Node({self.data})->{self.next}"


class Queue:
    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear


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


# Examples of using a queue
my_queue = Queue()

for i in range(1,6):
    my_queue.enqueue(i)

print(my_queue.front)
print(my_queue.rear)




"""
* Objective 4: Implementing a Stack using a Dynamic Array (a List in Python)

    - Two ways to implement a Stack:
        1. using a Linked List
        2. using a Dynamic Array

    * Dynamic Array (a List if using Python) Stacks:
        - push method adds to end of array (append)
        - pop method removes last element of array
"""

class Stack:
    def __init__(self, data=None):
        self.data = data


    def push(self, item):
        self.data.append(item)


    def pop(self):
        if len(self.data) > 0:
            return self.data.pop()
        
        return "Empty Stack"


    def peek(self):
        count = len(self.data)

        if count > 0:
            return self.data[count-1]

        return "Empty Stack"


# Examples of using a stack
my_data = [1,2,3,4,5]
my_stack = Stack(my_data)

print(my_stack.data)
print(my_stack.peek())
print(my_stack.data)
print(my_stack.pop())
print(my_stack.data)

my_stack.push(my_stack.peek())
print(my_stack.data)




"""
Objective 5: Implementing a Stack with a Linked List

    * Linked List stacks:
        - push method adds node to head of linked list
        - pop method removes node at head of list
        

    ** Note: Stacks built on top of either data structue (Dynamic Array or Linked List):
        - function in the same manner: LIFO

        * Linked List Stack works on FRONT of data structure
            - push/pop/peek head of linked list

        * Dynamic Array Stacks work on REAR of data structure
            - push/pop/peek at end of the array
"""

class LinkedListStack:
    def __init__(self, top=None):
        self.top = top


    def push(self, data):
        new_node = LinkedListNode(data)

        new_node.next = self.top
        self.top = new_node


    def pop(self):
        if self.top is not None:
            popped_top = self.top
            self.top = popped_top.next

        return popped_top.data


    def peek(self):
        if self.top is not None:
            return self.top.data

        return "Empty Stack"


# Examples of using a Stack built with a Linked List
my_ll_stack = LinkedListStack()

for i in range(1,6):
    my_ll_stack.push(i)

print(my_ll_stack.top)
print(my_ll_stack.pop())
my_ll_stack.push(my_ll_stack.peek())
print(my_ll_stack.top)