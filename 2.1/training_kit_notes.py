
"""
Sprint 2.1 - Array & String Manipulation
"""


"""
Objective 1: Time & space complexity, strengths & weaknesses, basic array operations

- Python does not have a static array data type
    - But the list type is built on dynamic arrays (which rely on static arrays underneath)


* Static arrays are a data type designed for storing info sequentially

    Time Complexity:
    
        - Lookups: using a specific index are O(1) constant time

        - Appends: adding to end is O(1) constant time
            - we always have a reference point to the last element in a static array
        
        - Insertions: adding to front or within an array is O(n) linear
            - rely on computations to shift all elements in memory beyond point of insertion

        - Deletions: if removing from the end O(1). Beginning or within the array is O(n)
            - static arrays rely on sequential elements, so must fill empty spaces by shifting


    Space Complexity:
        -  O(n) linear as each element takes up space in memory


    Strengths (when to use):
        1. retrieving by specific index
            - getting element at index is O(1) based on simple calculation:
            element = starting index + (size of each item * index)

        2. adding items to a data structure
            - adding items to end while gathering data is O(1)

    
    Weaknesses (when to avoid):
        1. when the amount of data is not known
            - not good when size/amount of information is frequent to change
            - running out of space in memory demands copying all elements to a new larger array

        2. if you plan to add at beginning or within the array
            - avoid using unless you'll only be adding data to end of array


    Array Slicing:
        * this handy tool is not a free operation, use wisely!

        1. first step allocates space for a new array in memory
            - O(n) space complexity

        2. second step is copying data from original array to newly allocated array
            - O(n) time complexity

    
    Additonal Resources:
        https://www.hackerearth.com/practice/data-structures/arrays/1-d/tutorial/
        https://www.pythoncentral.io/how-to-slice-listsarrays-and-tuples-in-python/
"""



"""
Objective 2: In-place vs out-of-place algorithms

    * In-place functions modify or destroy the state of the input data
        - this is more space efficient than allocating space for new array
        - space bonus comes with a trade off:
            - risk of unintentionally altering the data and destorying previous state

    * Out-of-place functions protect the state and data of original array
        - adds space complexity but prevents unwanted modifications to input


        ** When to use in-place vs out-of-place?
            - best to default to out-of-place
            - only use in-place when explicitly told to or need to preserve space


    Pass by reference vs pass by value:
        
        * Pass by value (primitive types)
            - integers, floats, strings
            - cannot change original object in memory

        * Pass by reference (non-primitve types)
            - lists, dictionaries
            - passed into function as a reference to original object in memory
                - changes made to named parameter will alter original object
                - create a copy to prevent unintended changes to state/data

        
    Additonal Resources:
        https://www.techiedelight.com/in-place-vs-out-of-place-algorithms/
"""