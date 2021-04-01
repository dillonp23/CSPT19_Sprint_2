
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
                    - divides collection in halfm then merges sorted halves
                
                3. perfect binary trees
                    - number of nodes doubles at each level
"""