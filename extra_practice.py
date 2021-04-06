

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
"""

def findTargetInPivotedArray(nums, target):
    start, end = 0, len(nums)-1

    if nums[start] == target:
        return start

    pivot_index = getPivotIndex(nums, start, end)

    if nums[pivot_index] == target:
        return pivot_index

    if nums[start] <= target and target < nums[pivot_index]:
        return sortedBinarySearch(nums, start, pivot_index, target)
    else:
        return sortedBinarySearch(nums, pivot_index, end, target)


# helper 1:
# looking for pivot -> index where nums[i] > nums[i+1]
# use recursion to narrow search
def getPivotIndex(nums, start, end):
    # base cases
    if start > end:
        return -1
    if start == end:
        return start

    mid = (start + end) // 2

    # Check if mid or mid-1 is pivot point and return index
    if mid < end and nums[mid] > nums[mid+1]:
        return mid
    elif mid > start and nums[mid] < nums[mid-1]:
        return mid-1

    # if no pivot found yet, recursively call
    if nums[start] >= nums[mid]:
        return getPivotIndex(nums, start, mid-1)
    else:
        return getPivotIndex(nums, mid+1, end)


# helper 2:
def sortedBinarySearch(nums, start, end, target):
    pass



print("Exercise 1: Find Target Index In Pivoted Array") 
# nums = [4,5,1,2,3], target = 3 ==>> expected: 4
# nums = [8,9,10,11,12,13,14,15,16,1,2,3,4,5,6,7], target = 2 ==>> expected: 10
# nums = [60...100, 1...59], target = 12 ==>> expected: 41
nums = []
for i in range(23, 101):
    nums.append(i)
for i in range(1, 23):
    nums.append(i)

print(nums)
print(findTargetInPivotedArray(nums, 22))