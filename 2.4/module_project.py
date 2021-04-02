
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

    fib_nums = [0,1]
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
print(fibonacciSimpleSum2(1)) # expected: True
print(fibonacciSimpleSum2(11)) # expected: True
print(fibonacciSimpleSum2(60)) # expected: True
print(fibonacciSimpleSum2(66)) # expected: False
print(fibonacciSimpleSum2(144)) # expected: True
print(fibonacciSimpleSum2(1928372849)) # expected: False




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