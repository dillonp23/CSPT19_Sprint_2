
"""
Sprint 2 - Module 3: Stack & Queues

* Queues
    - FIFO (First-in, First-out)
    - Analogous to a line or queue in real life

    
    Time Complexity:

        * Enqueue: O(1) - constant time
            - adds item to back of queue

        * Dequeue: O(1) - constant time
            - remove item from front of queue

        * Peek: O(1) - constant time
            - inspect item at front of queue without removing

    
    Space Complexity:

        * O(n) - linear space
            - each item in queue will take up space in memory

    
    Strengths:
        - primary strength is that all of its operations are fast O(1) - constant

    
    Weaknesses:
        - there are no specific weaknesses with queues
        - very targeted data structure designed to do only a few things well


    When to use queues?
        - useful in instances where you need FIFO order of operations
        - example use cases:
            
            * Web server
                - process and respond to requests in order received
            
            * Breadth-first traversal
                - a method of traversing heirachical data structures
                - queues can be used to facillitate this type of traversal
"""