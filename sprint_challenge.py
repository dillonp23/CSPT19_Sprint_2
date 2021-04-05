
"""
Sprint Challenge #2 - Data Structures and Algorithms I
"""


"""
Exercise 1: Reverse a Linked List (Task 1 of 9)

Given a singly linked list, reverse and return it.

* Notes: 
    - your solution should have O(n) time complexity and O(1) space complexity

* Example:
    For l = [1, 2, 3, 4, 5], the output should be
    reverseLinkedList(l) = [5, 4, 3, 2, 1]
"""

class ListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"{self.value}->{self.next}"


def reverseLinkedList(l):
    curr = l
    prev = None

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    
    return prev


print("Exercise 1: Reverse a Linked List")
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)

a.next = b
b.next = c
c.next = d

print(a)
b = reverseLinkedList(a)
print(b)




"""
Exercise 2: Check Blanagrams (task 4 of 9)

Two words are blanagrams if they are anagrams, but exactly one letter has been substituted for another.

Given two words, check if they are blanagrams of each other.

* Examples:
    For word1 = "tangram" and word2 = "anagram"
    checkBlanagrams(word1, word2) = true

    After changing the first letter 't' to 'a' in word1, the words become anagrams.


    For word1 = "tangram" and word2 = "pangram"
    checkBlanagrams(word1, word2) = true

    Since a word is an anagram of itself (a so-called trivial anagram), we are not obliged to rearrange letters. 
    Only the substitution of a single letter is required for a word to be a blanagram, and here 't' is changed to 'p'.


    For word1 = "aba" and word2 = "bab"
    checkBlanagrams(word1, word2) = true

    You can take the first letter 'a' of word1 and change it to 'b', obtaining the word "bba", which is an anagram 
    of word2 = "bab". It is also possible to change the first letter 'b' of word2 to 'a' and obtain "aab", which 
    is an anagram of word1 = "aba".


    For word1 = "silent" and word2 = "listen"
    checkBlanagrams(word1, word2) = false

    These two words are anagrams of each other, but no letter substitution was made (the trivial substitution of a letter 
    with itself shouldn't be considered), so they are not blanagrams.
"""

# words must be same length -> else return false
# a single letter change to word1 should return true if the count of all letters in both words are the same
# if the words are already anagrams of each other, then return false -> changing a letter will make them not
# if difference between letter counts != 1 (only one letter change) then return false 

# convert letters of word1 into a list
# iterate through letters of word2
    # if the letter appears in the list, remove first occurence
    # otherwise increment a count variable
# return count == 1 (false if more than 1 difference)

def checkBlanagrams(word1, word2):
    if len(word1) != len(word2):
        return False

    list_1 = []
    count = 0

    for letter in word1:
        list_1.append(letter)
    
    for letter in word2:
        try:
            list_1.remove(letter)
        except:
            count += 1


    return count == 1



print(checkBlanagrams("aba", "aba")) # expected: False
print(checkBlanagrams("abc", "aba")) # expected: True
print(checkBlanagrams("ab", "aba")) # expected: False
print(checkBlanagrams("testint", "testing")) # expected: True




"""
Exercise 3: Find Pivot Point (task 7 of 9) 

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
"""

# UPER - Plan:

# helper function_1: bin search to find pivot point
# helper function_2: bin search to find target index in full input array or subarray

# function 1:
# search for index where the array is pivoted using single pass binary search
# pivot index will be the index where the value to the right is smaller than it (since input is ascending)
# i.e. nums[pivot] > nums[pivot + 1]

# once we find pivot index, divide input into subarray from start-> pivot or pivot->end

# determine which subarray to perform bin search for target index
# if nums[start] < target and target < nums[pivot]
    # return bin search from nums[start:pivot] (function_2)

# return bin search for target in nums[pivot:end] (function_2)
# we're using the full nums array (only adjusting start/end), so we can directly return the result index from above
# this will return the index from w/in the second half of array, or -1 if target not in full array

def findTargetInPivotedArray(nums, target):
    start, end = 0, len(nums) - 1

    pivot_index = findPivot(nums, start, end)

    if nums[pivot_index] == target:
        return pivot_index

    if nums[0] == target:
        return 0

    if nums[start] < target and target < nums[pivot_index]:
        return sortedBinarySearch(nums, start, pivot_index, target)
    
    return sortedBinarySearch(nums, pivot_index, end, target)


def findPivot(nums, start, end):
    if end < start:
        return -1
    if start == end:
        return start

    mid = (start + end) // 2

    # compare values adjacent to index to see if either are pivot
    # index where nums[index] > nums[index + 1] is pivot
    if mid < end and nums[mid] > nums[mid + 1]:
        return mid
    if mid > start and nums[mid] < nums[mid - 1]: 
        return mid - 1

    # if no pivot found, continue recursing by adjusting start or end index
    if nums[start] >= nums[mid]:
        return findPivot(nums, start, mid - 1)
    else:
        return findPivot(nums, mid + 1, end)


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



print("\nExercise 3:")
nums = []
for i in range(60,101):
    nums.append(i)
for i in range(0,60):
    nums.append(i)

print(findTargetInPivotedArray(nums, 60)) # expected: 0
print(findTargetInPivotedArray(nums, 61)) # expected: 1
print(findTargetInPivotedArray(nums, 59)) # expected: 100
print(findTargetInPivotedArray(nums, 70)) # expected: 10
print(findTargetInPivotedArray(nums, 50)) # expected: 91
print(findTargetInPivotedArray(nums, 30)) # expected: 71