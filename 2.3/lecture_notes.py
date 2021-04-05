

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

    def __init__(self):
        self.data = deque()
        self.min = float("inf")


    def push(self, item):
        if item <= self.min:
            self.min = item

        self.data.append(item)


    def pop(self):
        popped = self.data.pop()
            
        if popped == self.min:
            if len(self.data) > 0:
                self.min = min(self.data)
            else:
                self.min = float("inf")
    

    def top(self):
        return self.data[-1]


    def getMin(self):
        return self.min



print("\nExercise 1:")
min_stack = MinStack()

min_stack.push(0)
min_stack.push(1)
min_stack.push(0)
print(min_stack.data)

print(min_stack.getMin())
print(min_stack.data)

print(min_stack.pop())
print(min_stack.data)

print(min_stack.getMin())
print(min_stack.data)




"""
* Queues in Python:
    - FIFO (first in first out)
    - can be implemented using LinkedLists

    Two methods:
        1. enqueue(value): adds to back of queue

        2. dequeue(): removes from front of queue


    Time & Space Complexity:

        * access: O(n)
            - no indexing support
            - need to dequeue until we reach end of queue

        * search: O(n)

        * insertion/deletion: O(n)
            - uses linked list under the hood
"""

class QueueNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        if self.next is None:
            return f"{self.value}"

        return f"{self.value}<-{self.next}"


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = QueueNode(value)

        if self.tail == None:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

    def dequeue(self):
        if self.head is None:
            return

        temp = self.head.value
        self.head = self.head.next
            
        if self.head == None:
            self.tail = None
            
        return temp



print("\nExample of a Queue using Linked Lists:")
myQueue = Queue()
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
print(myQueue.head)

myQueue.dequeue()
print(myQueue.head)

myQueue.dequeue()
print(myQueue.head)




"""
* Queue implementations can be simplified by using a deque data structure vs a linked list
"""

class MyDeque:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        self.queue.popleft()



print("\nExample of a Queue using deque in Python:")
myQueue = MyDeque()
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
print(myQueue.queue)

myQueue.dequeue()
print(myQueue.queue)

myQueue.dequeue()
print(myQueue.queue)




"""
Exercise 2: "225. Implement Stack using Queues" (https://leetcode.com/problems/implement-stack-using-queues/)

Implement a last in first out (LIFO) stack using only two queues. The implemented stack should support all the 
functions of a normal queue (push, top, pop, and empty).

* Implement the MyStack class:
    - void push(int x) Pushes element x to the top of the stack.
    - int pop() Removes the element on the top of the stack and returns it.
    - int top() Returns the element on the top of the stack.
    - boolean empty() Returns true if the stack is empty, false otherwise.

* Notes:
    - Use only standard operations of a queue: push to back, peek/pop front, size, and isEmpty operations
    - Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or 
        deque (double-ended queue), as long as you use only a queue's standard operations.
    

* Example:
    Input:
        ["MyStack", "push", "push", "top", "pop", "empty"]
        [[], [1], [2], [], [], []]

    Output:
        [null, null, null, 2, 2, false]

    Explanation:
        MyStack myStack = new MyStack();
        myStack.push(1);
        myStack.push(2);
        myStack.top(); // return 2
        myStack.pop(); // return 2
        myStack.empty(); // return False
"""

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        

    def top(self) -> int:
        """
        Get the top element.
        """
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
     


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()