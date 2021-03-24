
"""
Sprint 2.1 Lecture Notes - Array & String Manipulation

* Amoritzed = average time

* One con to in-place operations is potential for causing unintended side effects/bugs or corrupting data

* You cannot mutate a string without making a copy in python
"""



"""
Exercise 1: "66. Plus One" (https://leetcode.com/problems/plus-one/)

Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

 

* Example 1:
    Input: digits = [1,2,3]
    Output: [1,2,4]
    Explanation: The array represents the integer 123.
"""



"""
Exercise 2: "724. Find Pivot Index" (https://leetcode.com/problems/find-pivot-index/)

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers 
strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to 
the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.


* Example 1:
    Input: nums = [1,7,3,6,5,6]
    Output: 3
    Explanation:
    The pivot index is 3.
    Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
    Right sum = nums[4] + nums[5] = 5 + 6 = 11
"""