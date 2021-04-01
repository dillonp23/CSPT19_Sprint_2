

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




"""
Exercise 2: "374. Guess Number Higher or Lower" (https://leetcode.com/problems/guess-number-higher-or-lower/)

We are playing the Guess Game. The game is as follows:

    - I pick a number from 1 to n. You have to guess which number I picked.

    - Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

    - You call a pre-defined API int guess(int num), which returns 3 possible results:

    -1: The number I picked is lower than your guess (i.e. pick < num).
    1: The number I picked is higher than your guess (i.e. pick > num).
    0: The number I picked is equal to your guess (i.e. pick == num).
    Return the number that I picked.


* Examples:

    Input: n = 10, pick = 6
    Output: 6

    Input: n = 1, pick = 1
    Output: 1
"""