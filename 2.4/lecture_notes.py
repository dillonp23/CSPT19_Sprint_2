

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


* Hint: whenever you see the word "sorted" or "range of numbers" think binary search
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

    # start = 0
    # end = len(nums) - 1
    # ^ this can be simplified into a single line
    start, end = 0, len(nums) -1

    while start <= end:
        # use floor division '//' to make an int
        mid = (start + end) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            # start moves to the right, end stays same
            start = mid + 1
        else:
            # start stays same, end moves left
            end = mid - 1


    return -1


print("Exercise 1:")
nums = [0,2,7,8,10,13,22,43,45,56,62,73,80,92,102]
print(search(nums, 2))
print(search(nums, 10))
print(search(nums, 12))
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

    - Return the number that I picked.


* Examples:

    Input: n = 10, pick = 6
    Output: 6

    Input: n = 1, pick = 1
    Output: 1
"""
def guess(num) -> int:
    # defined by Leetcode behind scenes
    pass

def guessNumber(n):
    start, end = 1, n

    while start <= end:
        mid = (start + end) // 2
        result = guess(mid)

        if result == 0:
            return mid
        elif result == -1:
            end = mid - 1
        else:
            start = mid + 1


    return -1




"""
Exercise 3: "278. First Bad Version" (https://leetcode.com/problems/first-bad-version/)

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest
version of your product fails the quality check. Since each version is developed based on the previous version, 
all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the 
following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to 
find the first bad version. You should minimize the number of calls to the API.


* Examples:

    Input: n = 5, bad = 4
    Output: 4

    Explanation:
    call isBadVersion(3) -> false
    call isBadVersion(5) -> true
    call isBadVersion(4) -> true
    Then 4 is the first bad version.


    Input: n = 1, bad = 1
    Output: 1
"""

def isBadVersion(n) -> bool:
    # defined by Leetcode behind scenes
    pass

def firstBadVersion(n):
    # input is a range of nums, up to n
    start, end = 0, n

    while start <= end:
        mid = (start + end) // 2

        if isBadVersion(mid):
            end = mid - 1
        else:
            start = mid + 1

    return start




"""
* Recursion
    - a function that calls itself
    - can be elegant when doing repetitive work
    - a fractal pattern is a pattern that produces a picture which contains an infinite amount of copies of itself


    * the base case is the simplest case which returns in order to stop the recursive calls
        - not having proper base cases will cause an infinite loop
        - run out of memory, and cause a stack overflow
        - function will error out


    * IN ANY RECURSIVE FUNCTION:
        - first task is to define base case(s)!
        - base case is when we want recursion to stop

* Example of a use case:
    - factorial function
    - binary search with recursion
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n-1)


print("\nExample 4 - Factorial Recursively:")
print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(3))



# return the value of the nth number in fibonacci sequence
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)


print("\nExample 5 - Fibonacci Recursively:")
print(fibonacci(3))
print(fibonacci(10))
print(fibonacci(13))
print(fibonacci(20))




"""
* Downsides to recursion
    - can get complicated very quickly
    - can have a high space complexity

* What could you do instead?
    - dynamic programming!

    * one dynamic programming technique is called tabulation
"""
# tabulation example
def tabFib(n):
    fibs = [0,1]

    for i in range(2, n + 1):
        fibs.append(fibs[i - 1] + fibs[i - 2])

    return fibs[n]


print("\nExample 6 - Tabulation for Fibonacci:")
print(fibonacci(3))
print(fibonacci(10))
print(fibonacci(13))
print(fibonacci(20))




"""
We will be doing the same binary search challenge as exercise 1, but this time using recursion!

Exercise 4: "704. Binary Search" (https://leetcode.com/problems/binary-search/)

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.


* Example:
    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4
"""
# Solve with recursion - two functions
# Pretty common to use a 2nd helper function with recursion
def recursiveBinSearch(nums, target):
    return searchHelper(nums, 0, len(nums) - 1, target)


def searchHelper(nums, start, end, target):
    # base case => if we've searched entire list, we need to stop recursive calls
    # equivalent to "while start <= end" in iterative binary search of example 1
    if start > end:
        return -1
    
    # floor divison to get int (not float)
    mid = (start + end) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return searchHelper(nums, mid + 1, end, target)
    else:
        return searchHelper(nums, start, mid - 1, target)


print("\nExercise 4 - Binary Search Using Recursion:")
nums = [0,2,7,8,10,13,22,43,45,56,62,73,80,92,102]
print(recursiveBinSearch(nums, 2))
print(recursiveBinSearch(nums, 10))
print(recursiveBinSearch(nums, 12))
print(recursiveBinSearch(nums, 73))