

"""
Sprint 2.2 Lecture Notes - Linked Lists

- can hold any type of data, but usually contain a character (string) or a number (int)

* Singly linked list properties:
    1. data (typically string or int)
    2. next (reference to next node or None)

* Doubly linked list properties:
    1. data
    2. next
    3. prev (link to previous node)

* A linked list could also have a cycle in it
    - whether the entire list or a portion of it is cyclical
    - if cyclical then we never reach end of list as it just loops back around
"""

class LinkedListNode:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
    
    def __repr__(self):
        return f"Node({self.value})->{self.next}"


a = LinkedListNode(1)
b = LinkedListNode(2)
c = LinkedListNode(3)

a.next = b
b.next = c


def traverseLinkedList(startNode):
    curr = startNode
    print(f"full list: {curr}")

    while curr != None:
        print(curr)
        curr = curr.next

 
traverseLinkedList(a)