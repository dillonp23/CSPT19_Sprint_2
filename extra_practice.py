

"""
* Exercise 3 from Sprint Challenge: Find Pivot Point (task 7 of 9) 

You are given a sorted array in ascending order that is rotated at some unknown pivot (i.e., [0,1,2,4,5,6,7] might 
become [4,5,6,7,0,1,2]) and a target value.

Write a function that returns the target value's index. If the target value is not present in the array, return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

* Examples:
    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4

    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1


* UPER:

    * input:
        1. sorted array in ascending order
            - array is pivoted at some unkown point
        2. target value

    * output:
        - return the index if target val in array or -1 if not

    * highlights:
        - array in ascending order so we can use a modified binary search algo
            - needs to be modified as there is a pivot point
        - characteristics of the pivot point:
            - nums[pivot_index] will be greater than nums[pivot_index+1] as ascedning order
            - only one pivot point

    * plan:
        - use a modified binary search to find the pivot point in the array
        - after getting pivot point we can separate the array into two halves
        - determining if target val in lhs or rhs:
            - if target between lhs[0] and lhs[pivot_index]
                - do binary search with start = 0 and end = pivot_index
            else:
                - start = pivot_index and end = len(array)-1
        - utilize primary function and two helpers
            - 1st helper: modified binary search to find pivot_index
            - 2nd: standard bin search (using pivot_index as start or end) to find target


* test cases:
    1. nums = [4,5,1,2,3], target = 3 ==>> expected: 4
    2. nums = [8,9,10,11,12,13,14,15,16,1,2,3,4,5,6,7], target = 2 ==>> expected: 10
    3. nums = [60...100, 1...59], target = 12 ==>> expected: 53
"""

def findTargetInPivotedArray(nums, target):
    start, end = 0, len(nums)-1

    if nums[start] == target:
        return start
    elif nums[end] == target:
        return end

    pivot_index = getPivotIndex(nums, start, end)

    if nums[pivot_index] == target:
        return pivot_index

    if nums[start] <= target and target < nums[pivot_index]:
        return sortedBinarySearch(nums, start, pivot_index, target)
    
    return sortedBinarySearch(nums, pivot_index+1, end, target)



#  recursive implementation
# def getPivotIndex(nums, start, end):
#     # base cases
#     if start >= end:
#         return start

#     mid = (start + end) // 2

#     # Check if mid or mid-1 is pivot point and return index
#     if nums[mid] > nums[mid+1]:
#         return mid
#     elif nums[mid] < nums[mid-1]:
#         return mid-1

#     # if no pivot found yet, recursively call
#     if nums[start] >= nums[mid]:
#         return getPivotIndex(nums, start, mid-1)
#     else:
#         return getPivotIndex(nums, mid+1, end)



#  iterative implementation vs recursive
def getPivotIndex(nums, start, end):
    while start <= end:
        mid = (start + end) // 2

        if mid + 1 <= (len(nums) - 1) and nums[mid] > nums[mid + 1]:
            return mid
        elif nums[mid] < nums[mid - 1]:
            return mid - 1

        if nums[start] >= nums[mid]:
            end = mid - 1
        else:
            start = mid + 1

    # not searching for target index. return start (not -1)
    # start will be equal to last element in array if no pivot point
    return start



def sortedBinarySearch(nums, start, end, target):
    while start <= end:
        mid = (start + end) // 2

        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return -1



print("Exercise 1: Find Target Index In Pivoted Array") 
nums = [1,3]
print(findTargetInPivotedArray(nums, 3)) # expected: 1

nums = [8,9,10,11,12,13,14,15,16,1,2,3,4,5,6,7]
print(findTargetInPivotedArray(nums, 2)) # expected: 10

nums = []
for i in range(60,101):
    nums.append(i)
for i in range(0,60):
    nums.append(i)

print(findTargetInPivotedArray(nums, 12)) # expected: 53

# Additional test cases:
print(findTargetInPivotedArray(nums, 60)) # expected: 0
print(findTargetInPivotedArray(nums, 61)) # expected: 1
print(findTargetInPivotedArray(nums, 59)) # expected: 100
print(findTargetInPivotedArray(nums, 70)) # expected: 10
print(findTargetInPivotedArray(nums, 50)) # expected: 91
print(findTargetInPivotedArray(nums, 30)) # expected: 71

nums = [5,1,2,3,4]
print(findTargetInPivotedArray(nums, 1)) # expected: 1

nums = [1,3]
print(findTargetInPivotedArray(nums, 2)) # expected: -1

nums = [3,1]
print(findTargetInPivotedArray(nums, 1)) # expected: 1




"""
Exercise 2: "707. Design Linked List" (https://leetcode.com/problems/design-linked-list/)

Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, 
and next is a pointer/reference to the next node.

If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node 
in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:
    - MyLinkedList() Initializes the MyLinkedList object

    - int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1

    - void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, 
        the new node will be the first node of the linked list

    - void addAtTail(int val) Append a node of value val as the last element of the linked list

    - void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index 
        equals the length of the linked list, the node will be appended to the end of the linked list. If index is 
        greater than the length, the node will not be inserted

    - void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid
 

* Example:

    Input:
        ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
        [[], [1], [3], [1, 2], [1], [1], [1]]
    Output:
        [null, null, null, null, 2, null, 3]

    Explanation:
    MyLinkedList myLinkedList = new MyLinkedList()
    myLinkedList.addAtHead(1)
    myLinkedList.addAtTail(3)
    myLinkedList.addAtIndex(1, 2)    # linked list becomes 1->2->3
    myLinkedList.get(1)              # return 2
    myLinkedList.deleteAtIndex(1)    # now the linked list is 1->3
    myLinkedList.get(1)              # return 3
"""

class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        if self.next is None:
            return f"{self.val}->None"

        return f"{self.val}->{self.next}"


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None


    def __repr__(self):
        return f"{self.head}"


    def get(self, index: int) -> int:        
        count = 0
        curr = self.head

        while curr:
            if index == count:
                return curr.val
            else:
                curr = curr.next
                count += 1

        return -1
        

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            return self.addAtHead(val)

        curr = self.head
        next = curr.next
        count = 1

        while next:
            if index == count:
                new_node = ListNode(val)
                new_node.next = next
                curr.next = new_node
                return
            
            curr = next
            next = curr.next
            count += 1

        if next is None and curr is not None: 
            if count == index:
                self.addAtTail(val)

    """
    input_list = 1-2-3-5 // addAtIndex(3, 4):

        if index == 0:
                return self.addAtHead(val)

        ||curr = 1
        ||next = 2
        ||count = 1

        ||while next:
        ||      1-2-3-5
        ||   1. ^ ^ count = 1 ==>> curr = 2, next = 3, count = 2
        ||   2.   ^ ^ count = 2 ==>> curr = 3, next = 5, count = 3
        ||   3.     ^ ^ count = 3 ==>> curr = 5, next = None, count = 4
        ||   4. return // list = 1-2-3-4-5

        if next == None and curr != None:
            count == index:
                return self.addAtTail(val)
    """


    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return
        
        curr = self.head
        prev = None
        count = 0

        while curr:
            if count == index:
                temp = curr.next
                if count == 0:
                    self.head = temp
                    if self.head is None:
                        self.tail = None
                else:
                    prev.next = temp
                    if temp is None:
                        self.tail = prev
                return
            else:
                prev = curr
                curr = curr.next
                count += 1


print("\nExercise 2: Custom Linked List Implementation")
my_list = MyLinkedList()
my_list.addAtHead(5)
my_list.addAtHead(3)
my_list.addAtHead(2)
my_list.addAtHead(1)
print(my_list)  # expected: 1->2->3->5->None
print(my_list.get(3))  # expected: 5
my_list.addAtIndex(3, 4)
print(my_list)  # expected: 1->2->3->4->5->None
my_list.addAtHead(0)
my_list.addAtTail(6)
my_list.addAtIndex(7, 7)
print(my_list)  # expected: 0->1->2->3->5->6->7->None
my_list.deleteAtIndex(7)
print(my_list)  # expected: 0->1->2->3->5->6->None
my_list.deleteAtIndex(0)
print(my_list)  # expected: 1->2->3->5->6->None
my_list.addAtIndex(7, 8)
print(my_list)  # expected: 1->2->3->5->6->None (no change from previous)