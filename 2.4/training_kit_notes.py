
"""
Sprint 2.4 - Searching & Recursion


Objective 1: Understanding Logarithms

    * Logarithms:
        - have an inverse relationship to exponents, just like division & multiplication
        - what factors we know determine when to use logarithm vs exponents
            - if we know the growth rate, and time spent growing => exponents
            - if we know where we end up and growth rate => logarithm


            2^5 = x 
                -- the base, 2, represents the growth rate ==>> i.e. doubling each time
                -- the exponent, 5, represents the # of times we go through the growth
                -- the answer, x (32 in this case), represents where we end up

            
            log_2(32) = x
                -- log base of 2 == growth rate
                -- 32 is where we end up
                -- the answer, x (5 in this case), is number of times we go through the growth


        * Whats the significance?
            - in CS you'll often encounter questions like:
                - "how many times must n be divided in half before we get to one?"
                - "how many times will collection be halved before collection has one item?"
    
            * Hint *
                - any algorithm that doubles or halves a number or collection on each loop iteration
                    is likely to have O(log n)
                

        * Examples:

                1. binary search algorithms

                2. merge sort algorithms 
                    - divides collection in half then merges sorted halves
                
                3. perfect binary trees
                    - number of nodes doubles at each level



Objective 2: Linear Search Algorithm

Imagine that I've chosen a random number from 1 to 20. Then, you must guess the number. One approach would be to start 
picking at 1 and increment your guess by 1 with each guess. If the computer randomly selected 20, then it would take 
you 20 guesses to get the correct answer. If the computer guessed 1, then you would have the right answer on your very 
first guess. On average, you will get the correct answer on the 10th or 11th guess.

If the collection we are searching through is random and unsorted, linear search is the most efficient way to search 
through it. Once we have a sorted list, then there are more efficient approaches to use.


Write a simple program to conduct a linear search on a collection of data.
"""

def linear_search(arr, target):

    # loop through and check if item in input array is the target
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        
    # if target not in array return index out of range
    return -1


example_arr = [12,4,5,25,9,7,3,1,2]
target_1 = 8
target_2 = 9
target_3 = 0
target_4 = 10

print(linear_search(example_arr, target_1))
print(linear_search(example_arr, target_2))
print(linear_search(example_arr, target_3))
print(linear_search(example_arr, target_4))