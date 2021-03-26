

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


"""
Exercise 1: "237. Delete Node in a Linked List" (https://leetcode.com/problems/delete-node-in-a-linked-list/)

Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list, 
instead you will be given access to the node to be deleted directly.

It is guaranteed that the node to be deleted is not a tail node in the list.

* Example:
    Input: head = [4,5,1,9], node = 5
    Output: [4,1,9]
    Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
"""

def deleteNode(self, node):
    next = node.next
    node.val = next.val
    node.next = next.next


# modifying node in place - don't return anything
# the given node will be associated with a list, but we will not know the list elements or be given the head




"""
Exercise 2: "206. Reverse Linked List" (https://leetcode.com/problems/reverse-linked-list/)

Given the head of a singly linked list, reverse the list, and return the reversed list.

* Examples:
    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]
"""

def make_linked_list(input_list):
    head = None
    prev = None

    for item in input_list:
        new_node = LinkedListNode(item)

        if head is None:
            head = new_node
            prev = head
        else:
            prev.next = new_node
            prev = new_node

    return head


def resultNodes(head):
    
    while head:
        return str(head.value) + "->" + str(resultNodes(head.next))
    else:
        return None


def reverseList(head):
    prev = None
    curr = head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev


# Examples and test cases:
a = make_linked_list([0,1,2,3,4])
reversed_a = reverseList(a)
print(resultNodes(reversed_a))

b = make_linked_list([])
reversed_b = reverseList(b)
print(resultNodes(reversed_b))

c = make_linked_list([3,5,7,9,22])
reversed_c = reverseList(c)
print(resultNodes(reversed_c))

d = make_linked_list([100,95,90,85,80,75])
reversed_d = reverseList(d)
print(resultNodes(reversed_d))