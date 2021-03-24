
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

# def plusOne(digits):
#     carry = 1
#     i = len(digits) - 1
    
#     while i > 0:
#         curr_sum = digits[i] + carry
#         carry = int(curr_sum / 10)

#         digits[i] = curr_sum % 10
#         i -= i

#     print(carry)

#     if carry > 0:
#         digits.insert(0, carry)

    
#     return digits


# print(plusOne([1,2,9])) # => expected
# print(plusOne([9,9,9]))# => expected [1,0,0,0]
# print(plusOne([0]))


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

# the pivot index is not counted in the sum, i.e. it's the sum of digits to left and right

def pivotIndex(nums):
    rhs_sum = sum(nums)
    lhs_sum = 0

    for i, num in enumerate(nums):
        if i - 1 >= 0:
            lhs_sum += nums[i-1]

        rhs_sum -= num

        if lhs_sum == rhs_sum:
            return i

    return -1


print(pivotIndex([1,2,2,3])) # => expected: 2
print(pivotIndex([1,2,3])) # => expected: -1
print(pivotIndex([2,0,2])) # => expected: 1
print(pivotIndex([1,2,-2])) # => expected: 0
print(pivotIndex([-2,2])) # => expected: -1

# pivotIndex([2,0,-2]) => 1
# pivotIndex([1,2,-2]) => 0 =>> pivot index is zero, because sum to the left of pivot is 0 and sum to the right (-2 + 2 == 0)
# pivotIndex([-2,2]) => -1 =>> none because the pivot index would need to be between 0 and 1