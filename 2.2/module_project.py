
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