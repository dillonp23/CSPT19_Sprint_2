

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




"""
Exercise 3: "328. Odd Even Linked List" (https://leetcode.com/problems/odd-even-linked-list/)
    - Medium on LeetCode

Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes 
with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

* Examples:
    Input: head = [1,2,3,4,5]
    Output: [1,3,5,2,4]
"""

def group_nodes(head):
    head = make_linked_list(head)

    even_list = None
    even_prev = None

    odd_list = None
    odd_prev = None

    curr = head

    while curr:
        temp = curr.next

        if curr.value % 2 == 0:
            if even_list is None:
                even_list = curr
                even_prev = even_list
            else:
                even_prev.next = curr
                curr.next = None
                even_prev = curr

        elif curr.value % 2 != 0:
            if odd_list is None:
                odd_list = curr
                odd_prev = odd_list
            else:
                odd_prev.next = curr
                curr.next = None
                odd_prev = curr

        curr = temp


    if odd_prev:
        odd_prev.next = even_list
    else:
        return even_list
    

    return odd_list


# iterate through list
# if node is odd, go to next node
# if node is even, remove even node and append to an even_list
# after iterating through all nodes in head, append the evens list to head
# if the first node of the list is even and prev is None


group_1 = group_nodes([1,2,3,4,5,6]) # expected: None
print(group_1)

group_2 = group_nodes([0]) # expected: 0->None
print(group_2)

###
# Bug: Need to fix algorithm when input size is only 2
group_3 = group_nodes([2,1]) # expected: 1->2->None
# print(group_3)
###

group_4 = group_nodes([1,2,3,4,5]) # expected: 1->3->5->2->4->None
print(group_4)

group_5 = group_nodes([2,4,6,1,3,5]) # expected: 1->3->5->2->4->6->None
print(group_5)

group_6 = group_nodes([3,4,6,3,1,8,9]) # expected: 3->3->1->9->4->6->8->None
print(group_6)