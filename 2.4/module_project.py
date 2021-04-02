
"""
Sprint 2.4 - Binary Search & Recursion CodeSignal Assignment


* Task 1 (multiple choice):

Which logarithmic expression is identical to the following exponential expression?

    2^n = 64

* Answer:
    log_2(64) = n




* Task 2 (multiple choice):

When solving an algorithmic coding challenge, which keywords should you look out for that
might alert you that logarithims are involved?

* Answer:
    - divide in half
    - binary search
    - double




* Task 3 (multiple choice):

What type of search algorithm is used in this representation?

    1. {9-7-6-4-3-2-1} --- {6}

    2. {9-7-6-4-3-2-1} --- {4 < 6}
              ^
    3. {9-7-6}-4-3-2-1 --- {7 > 6}
          ^
    4. 9-7-{6}-4-3-2-1 --- {6 == 6}
            ^

* Answer:
    - binary search




* Task 4 (multiple choice):

Given an example of a binary search algorithm, what must be true?

    def binary_search(item_list, item):
        first = 0
        last = len(item_list) - 1

        while first <= last:
            mid = (first + last) // 2

            if item_list[mid] == item:
                return True
            else:
                if item < item_list[mid]:
                    last = mid - 1
                else:
                    first = mid + 1

        return False


* Answer:
    - item_list must be sorted from smallest to greatest
"""


"""
Exercise 1 (task 5 of 7):

For a given positive integer n, determine if it can be represented as a sum of two Fibonacci numbers (possibly equal).

* Examples:

    1.  For n = 1, the output should be
        fibonacciSimpleSum2(n) = true

        Explanation: 1 = 0 + 1 = F0 + F1


    2.  For n = 11, the output should be
        fibonacciSimpleSum2(n) = true

        Explanation: 11 = 3 + 8 = F4 + F6


    3.  For n = 60, the output should be
        fibonacciSimpleSum2(n) = true

        Explanation: 60 = 5 + 55 = F5 + F10


    4.  For n = 66, the output should be
        fibonacciSimpleSum2(n) = false
"""

# UPER - Plan:
# if n == 1, return True

# build a list (starting with [0,1]) of all fibonacci numbers up to n using the tabulation method
# use an index pointer to iterate in while loop

# since 'n' is the target sum, we only want to loop while the last number in fib sequence is < n
# i.e. we don't want to iterate UP TO N numbers ==>> iterate until the last value is greater than or equal to n

# before adding the new numbers to the list, set 'tagret_num = n - curr_fib'
   # check if target_num is < curr_fib_num
       # use a helper function to pass fib_nums list & target_num
       # if target_num is in list w/ binary search, return True


def fibonacciSimpleSum2(n):
    if n == 1:
        return True

    fib_nums = [0, 1]
    i = 2

    # continue looping until the last number in fib_nums is >= n
    while fib_nums[-1] < n:
        curr_fib_num = fib_nums[i - 1] + fib_nums[i - 2]
        target_num = n - curr_fib_num

        if target_num < curr_fib_num:
            result = fibSumHelper(fib_nums, target_num)

            if result + curr_fib_num == n:
                return True

        fib_nums.append(curr_fib_num)
        i += 1

    return False


def fibSumHelper(nums, target):
    start, end = 0, len(nums) - 1

    while start <= end:
        mid = (start + end) // 2
        result = nums[mid]

        if result == target:
            return result
        elif result < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1


print("Exercise 1 - Two Sum Fibonacci:")
print(fibonacciSimpleSum2(1))  # expected: True
print(fibonacciSimpleSum2(11))  # expected: True
print(fibonacciSimpleSum2(60))  # expected: True
print(fibonacciSimpleSum2(66))  # expected: False
print(fibonacciSimpleSum2(144))  # expected: True
print(fibonacciSimpleSum2(1928372849))  # expected: False


"""
Exercise 2 (task 6 of 7):

Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to
search for target in nums. If target exists, then return its index, otherwise return -1.

* Examples:

    1.  Input: nums = [-1,0,3,5,9,12], target = 9
        Output: 4
        Explanation: 9 exists in nums and its index is 4

    2.  Input: nums = [-1,0,3,5,9,12], target = 2
        Output: -1
        Explanation: 2 does not exist in nums so return -1

* Notes:
    All elements in nums are unique.
    The length of nums will be <= 100
    The value of each element in nums will be in the range [1, 10000]
"""

# UPER - Plan:
# keywords: *sorted, *ascending
# will be writing a simple binary search algo
# compare value at mid index
# if value < target ==> start = mid + 1
# else ==> end = mid -1

# output: return index or -1


def csBinarySearch(nums, target):
    start, end = 0, len(nums) - 1

    while start <= end:
        # use floor division to get integer for mid index
        mid = (start + end) // 2
        val = nums[mid]

        if val == target:
            return mid
        elif val < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1


print("\nExercise 2 - Simple Binary Search:")

nums_1 = [0, 1, 2, 3, 4, 5, 6, 7]
print(csBinarySearch(nums_1, 6))


nums_2 = [46, 176, 487, 551, 980, 1020, 1098, 1354, 1381, 1414, 1578, 1579, 1596,
          1634, 1810, 1882, 1924, 1999, 2021, 2074, 2083, 2269, 2579, 2616, 2626, 2645,
          2871, 2874, 2889, 2987, 2999, 3106, 3126, 3191, 3217, 3304, 3342, 3516, 3557,
          3579, 3617, 3655, 4022, 4049, 4059, 4386, 4510, 4600, 4792, 4799, 4937, 5257,
          5466, 5489, 5574, 5623, 5915, 5929, 5976, 6011, 6047, 6136, 6173, 6175, 6331,
          6333, 6368, 6631, 6673, 6847, 6960, 7034, 7042, 7167, 7186, 7352, 7604, 7879,
          7945, 7991, 8225, 8226, 8330, 8370, 8394, 8500, 8528, 8563, 8786, 8831, 8837,
          8861, 8976, 9236, 9251, 9388, 9436, 9532, 9708, 9891]
print(csBinarySearch(nums_2, 2871))


nums_3 = [163, 206, 622, 848, 962, 1029, 1299, 1321, 1386, 1405, 1551, 1567, 1613,
          1624, 1648, 1658, 2170, 2251, 2253, 2259, 2524, 2700, 2713, 2938, 3030, 3077,
          3327, 3363, 3373, 3517, 3544, 3710, 3712, 3716, 3724, 3758, 3800, 3865, 3873,
          4019, 4197, 4286, 4287, 4321, 4367, 4377, 4419, 4468, 4494, 4618, 4800, 4957,
          5148, 5156, 5175, 5443, 5502, 5510, 5525, 5793, 5798, 5969, 6120, 6289, 6698,
          6864, 6946, 7093, 7124, 7242, 7343, 7356, 7424, 7503, 7661, 7809, 7904, 8255,
          8387, 8390, 8451, 8460, 8541, 8582, 8595, 8646, 8697, 8719, 8771, 8800, 9141,
          9215, 9233, 9365, 9371, 9671, 9673, 9778, 9913, 9964]
print(csBinarySearch(nums_3, 1321))


nums_4 = [158, 227, 265, 311, 377, 661, 688, 802, 827, 829, 902, 1016, 1127, 1239,
    1243, 1422, 1549, 1554, 1620, 1739, 2001, 2043, 2228, 2292, 2393, 2499, 2517,
    2549, 2587, 2835, 2935, 2951, 3050, 3058, 3066, 3271, 3757, 3827, 3881, 3898,
    4012, 4049, 4109, 4244, 4663, 4678, 4712, 4792, 4803, 4993, 5081, 5122, 5322,
    5355, 5357, 5397, 5562, 5578, 5589, 5714, 5742, 5779, 5872, 5961, 6025, 6056,
    6096, 6129, 6418, 6428, 6434, 6621, 6732, 6735, 6883, 6958, 7239, 7250, 7261,
    7442, 7631, 7759, 7762, 7917, 8111, 8204, 8470, 8505, 8508, 8672, 8952, 9075,
          9097, 9248, 9467, 9532, 9598, 9885, 9933, 9997]
print(csBinarySearch(nums_4, 2385))


"""
Exercise 3 (task 7 of 7):

Given an integer array nums sorted in ascending order, and an integer target. Suppose that nums is rotated at some pivot
unknown to you beforehand (i.e., [1,2,4,5,6,7] might become [4,5,6,7,1,2]).

You should search for target in nums and if found return its index, otherwise return -1.

Your solution should have better than O(n) time complexity over the number of items in the list.
    - there is an O(log n) solution
    - there is also an O(1) solution

* Examples:

    1.  Input: nums = [6,7,1,2,3,4,5], target = 1
        Output: 2

    2.  Input: nums = [6,7,1,2,3,4,5], target = 3
        Output: 4

    3.  Input: nums = [1], target = 2
        Output: -1

* Notes:
    1 <= nums.length < 100
    1 <= nums[i] <= 100
    All values of nums are unique.
    Numbers from 1 up to the length of the list will be contained in the list.
"""

# UPER - Plan:
# keywords: *sorted, *ascending, *pivot
# NOTE: list will be all numbers in range(1, len(list))

#  Since list is in order from range(1, len(nums)):
    # value at middle index should be equal to ==>> mid + 1
    # i.e. expected value is mid + 1
    # the difference between expected value and actual determins shift

# positive ==> shifted left
# negative ==> shifted right

# [4,5,6,7,1,2,3] 
# value at mid = 1 
# expected value = mid + 1 ==> 4 + 1 = 5
# difference = expected - mid ==> 5 - 1 = 4

# target = 2
# expected_index = target - 1 ==> 2 - 1 = 1
# actual_index = expected_index + difference ==> 1 + 4 = 5


# [3,4,5,6,1,2]
# value at mid = 6
# expected value = mid + 1 ==> 4
# difference = expected - mid ==> 4 - 6 = -2

# target = 4
# expected_index = target - 1 ==> 4 - 1 = 3
# actual_index = expected_index + difference ==> 3 + (-2) = 1

def csSearchRotatedSortedArray(nums, target):
    count = len(nums) - 1
    mid_index = count // 2

    mid_val = nums[mid_index]
    expected_val = mid_index + 1
    # shifted to the right
    difference = expected_val - mid_val

    expected_index = target - 1
    actual_index = expected_index + difference

    if actual_index > count:
        actual_index -= len(nums)

    return actual_index


print("\nExercise 3 - Search Sorted & Rotated Array")
print(csSearchRotatedSortedArray([8,9,10,1,2,3,4,5,6,7], 4))

[1,2,3,4,5,6]

# target = 90
# expected index of target = 89
# nums[89] = 72

# nums[0] = 83 - 1 = 82
# len(nums) - 1 = 99 - 82 = 17

# if actual > len(nums):
#   actual -= count