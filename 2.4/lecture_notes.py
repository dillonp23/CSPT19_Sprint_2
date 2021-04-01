

"""
Sprint 2.4 Lecture Notes - Searching & Recursion

* Searching a collection for an item:
    - if a collection is sorted, then we can acheive better than O(n) run time when searching for an element in a collection
        - can also work if 'nearly' sorted


* Binary search algorithms:
    - halve the search space on each iteration
    - primary algo example of a logarithmic function

    Steps:
        1. Start at halfway of collection
        2. if that target then return index
        3. if not:
            a. if target is larger then somewhere to the right
            b. if target is smaller than to the right
        4. repeat


* Hint: whenever you see the word "sorted" think binary search
"""




"""
* Exercise 1: "704. Binary Search" (https://leetcode.com/problems/binary-search/)

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search
target in nums. If target exists, then return its index. Otherwise, return -1.

 
* Example:
    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4
"""

def search(nums, target):

    start, end = 0, len(nums) - 1

    while start <= end:
        mid = (start + end) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1


    return -1


nums = [0,13,22,43,45,56,62,73,80,92,102]
print(search(nums, 73))