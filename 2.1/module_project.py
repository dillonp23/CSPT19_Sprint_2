

"""
Sprint 2.1 Module Project - Arrays & String Manipulation


* Task 1 (multiple choice):

What are the two primary weaknesses of a static array as a data structure?

Answer:
    1. Fixed size
    2. O(n) insertions and deletions
        - when operation not at end of array



* Task 2 (multiple choice):

What is the time and space complexity of slicing an array in Python?

Answer:
    time: O(n)
        - due to iterating through the array
    space: O(n)
        - slicing in Python initializes a new array with the desired elements
        - leaves the original array data unaltered but sacrifices space to do so



* Task 3 (multiple choice):

Why are out-of-place algorithms generally considered to be safer?

Answer:
    - They avoid (unintended) side-effects



* Task 4 (free response):

In your own words, explain why the worst-case time cost of appending to a dynamic array is O(n)?

Answer:
    In the worst case scenario appending to a dynamic array is an O(n) time cost because the underlying data structure needs 
    to be copied to a new place in memory. Since arrays are represented as sequential slots in memory, if you fill all of the 
    spots in an array, in order to preserve the indexing benefits of the array you have to find a new place in memory. Each 
    time this happens the size of the array will be doubled and copy all of the previous elements before appending the new 
    element. This process is O(n) time complexity, however as the input size increases, the doubling process will occur less 
    and less frequently and therefore in the average case, appends to dynamic arrays are O(1).
"""