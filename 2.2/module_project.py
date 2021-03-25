
"""
Sprint 2.2 Module Project - Linked Lists


Exercise 1: Insert value into sorted linked list (task 3 of 4)

You have a singly linked list l, which is sorted in strictly increasing order, and an integer value. Add value to the 
list l, preserving its original sorting. Return l after inserting the new value.

Note: Your solution should have O(n) time complexity, where n is the number of elements in l, since this is what you 
will be asked to accomplish in an interview. 

* Examples:
    For l = 1-> 3-> 4-> 6 and value = 5, the output should be:
        insertValueIntoSortedLinkedList(l, value) = [1, 3, 4, 5, 6]

    For l = 1-> 3-> 4-> 6 and value = 10, the output should be:
        insertValueIntoSortedLinkedList(l, value) = [1, 3, 4, 6, 10]

    For l = 1-> 3-> 4-> 6 and value = 0, the output should be:
        insertValueIntoSortedLinkedList(l, value) = [0, 1, 3, 4, 6]
"""

class ListNode:

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


def resultNodes(head):
    
    while head:
        return str(head.value) + "->" + str(resultNodes(head.next))
    else:
        return None


# Step 1: Understand & Plan
    # def insertNewValue(list, value):
        # return l if no new value or new node if no l

        # prev = None
        # curr = l

        # while there is a current value:
            # 1st case => 
                # if prev is None:
                    # if new_node.value < curr.value:
                        # set new_node's next value to curr
                        # return new_node
                            
                    # if new_node.value > curr.value:
                        # curr.next = new_node
                        # break

            # 2nd case => 
                # prev.value < new_node.value and new_node.value < curr.value:
                    # new_node.next = curr
                    # prev.next = new_node
                    # break

            # 3rd case =>
                # if curr.next is None:
                # (we're at the tail of current list, so add new node)
                # curr.next = new_node
                # break

            # set prev to current
            # update current to next


def insertValueIntoSortedLinkedList(l, value):
    if value is None:
        return l

    new_node = ListNode(value)

    if l is None:
        return new_node

    prev = None
    curr = l

    while curr:
        
        if prev is None:
            if new_node.value < curr.value:
                new_node.next = curr
                return new_node
            
            if curr.next is None and new_node.value > curr.value:
                curr.next = new_node
                break

        else:
            
            if prev.value < new_node.value and new_node.value < curr.value:
                
                new_node.next = curr
                prev.next = new_node
                break

    
            if curr.next is None:
                curr.next = new_node
                break

        prev = curr
        curr = curr.next

    return l


# 1. insertValueIntoSortedLinkedList(None, 5) => expected: 5->None
test_1 = insertValueIntoSortedLinkedList(None, 5)
print(resultNodes(test_1))


# 2. insertValueIntoSortedLinkedList(1->3->4->6->None, 5) => expected: 1->3->4->5->6->None
a_2 = ListNode(1)
b_2 = ListNode(3)
c_2 = ListNode(4)
d_2 = ListNode(6)

a_2.next = b_2
b_2.next = c_2
c_2.next = d_2

test_2 = insertValueIntoSortedLinkedList(a_2, 5)
print(resultNodes(test_2))


# 3. insertValueIntoSortedLinkedList(239->None, 240) => expected: 239->240->None
a_3 = ListNode(239)
test_3 = insertValueIntoSortedLinkedList(a_3, 240)
print(resultNodes(test_3))


# insertValueIntoSortedLinkedList(1->3->4->5->6->None, 10) => expected: 1->3->4->5->6->10->None
test_4 = insertValueIntoSortedLinkedList(a_2, 10)
print(resultNodes(test_4))


# insertValueIntoSortedLinkedList(1->3->4->5->6->10->None, 0) => expected: 0->1->3->4->5->6->10->None
test_5 = insertValueIntoSortedLinkedList(a_2, 0)
print(resultNodes(test_5))




"""
Exercise 2: Merge Two Linked Lists (task 4 of 4)

Given two singly linked lists sorted in non-decreasing order, your task is to merge them. In other words, return 
a singly linked list, also sorted in non-decreasing order, that contains the elements from both original lists.

Note: Your solution should have O(l1.length + l2.length) time complexity, since this is what you will be asked 
to accomplish in an interview.

* Examples:
    For l1 = [1, 2, 3] and l2 = [4, 5, 6], the output should be
    mergeTwoLinkedLists(l1, l2) = [1, 2, 3, 4, 5, 6]

    For l1 = [1, 1, 2, 4] and l2 = [0, 3, 5], the output should be
    mergeTwoLinkedLists(l1, l2) = [0, 1, 1, 2, 3, 4, 5]
"""

# UPER:
    # Different cases
        # 1. all l1 < all l2
        # 2. uneven mix of (l1 < l2) and (l2 < l1)
        # 3. uneven counts of l1 and l2
        # 4. one list empty
        # 5. both lists empty

    # Plan approach
        # prev variable, curr variable (for both lists)
        # compare l1[0] and l2[0], use list with lower value, or l1 default if the same
        # iterate lists
            # at each node on new list compare l1_curr and l2_curr
            # temp variable to store either l1 or l2
            # l1 or l2 .next = None
            # add either l1 or l2 node, by doing new_node.next = curr, prev.next = new_node
            # set l1 or l2 = temp.next to iterate



mergeTwoLinkedLists([1], [0,2]) # expected: 0->1->2
mergeTwoLinkedLists([2], [0,1,3]) # expected: 0->1->2->3
mergeTwoLinkedLists([1,2,3], [4,5,6]) # expected: 1->2->3->4->5->6
mergeTwoLinkedLists([1,1,2,4], [0,3,5]) # expected: 0->1->1->2->3->4->5
mergeTwoLinkedLists([0,0,2], [1,1,3]) # expected: 0->0->1->1->2->3
mergeTwoLinkedLists([0,2,4,8], [1,3,5,7]) # expected: 0->1->2->3->4->5->7->8
mergeTwoLinkedLists([0,1,2,4], [0,1,3,5]) # expected: 0->0->1->1->2->3->4->5


