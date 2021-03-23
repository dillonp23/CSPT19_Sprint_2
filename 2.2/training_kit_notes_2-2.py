

"""
Sprint 2.2 - Linked Lists
"""


"""
Objective 1: Time/space complexity, strengths & weaknesses, and common uses of a linked list

    * Basic properties of a linked list:
        1. simple, linear data structure

        2. a collection of elements that doesn't require contiguous space in memory
            - can spread out data stored in memory

        3. made up of nodes holding both:
            - data
            - pointer to next node (or next and prev if doubly-linked)


    * What types of data can linked lists be used for?
        - strings, numbers, booleans, even other data structures
        - the type of data is not necessarily the limitng factor when it comes to linked lists

    
    * Are elements sorted or unsorted in linked list?
        - elements can be either or
        - nothing explicitly forces linked list to be sorted or not
        - knowing data is stored in a linked list does not tell you whether its sorted

    
    * Can linked lists contain duplicates?
        - yes
        - nothing prevents dupicates from being stored
            - in contrast to another structure like a Set

        
    * What are the different types of linked lists?
        - three different types, but all having same basic structure
        - node with data and pointer(s) to next (and prev) node(s)

        1. singly linked list (SLL)

        2. doubly linked list (DLL)

        3. circular linked list


    Singly linked lists:
        - can only navigate forward in SLL
        - to traverse, need to sart at reference to first node ("head")
        - from there, you can iterate through using each node's next pointer
        - reference to end of list is known as the "tail"

    
    Doubly linked lists:
        - can navigate forward and backwards
        - each node has reference to prev and next node in addition to data
        - stores reference to a head and tail as well

    
    Circularly linked list:
        - similar to DLL, but last node links back to first
        - causes a cyclical traversal through list



    * Time Complexity:

        - Lookups: using index is O(n) linear due to list traversal over each node

        - Appends: adding an item to end of list is O(1) constant
            - using reference to tail, easily insert after tail and update new tail

        - Insertions: in worst case O(n) due to list traversal over nodes

        - Deletions: in words case O(n) due to traversal

    
    * Space Complexity:
        - O(n) linear space complexity as each node takes up n space in memory


    
    * Strengths:
        - primary strength is that operations at ends are fast -> O(1) constant
            - we always have reference to head and tail
        
        - size of list can fluctuate, so knwoing how much space at init is not necessary
            - similar to dynamic array

        - a benefit as compared to dynamic arrays is LL's don't have doubling appends
            - since nodes are spread out in memory, doubling size and moving data not needed
            - whenever adding a new element, we just need to find space enough for single element
    

    * Weaknesses:
        - inability to efficiently access data at specific index every time
            - 0th index (head) is easy, but in middle or at end is not
            - in order to know if a LL has an element at index, we need to traverse list & count
            - no simple math to jump from first element to 7th like an array
"""