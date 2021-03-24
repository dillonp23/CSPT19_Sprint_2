
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