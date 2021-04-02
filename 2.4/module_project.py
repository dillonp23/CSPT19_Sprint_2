
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