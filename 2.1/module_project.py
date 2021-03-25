

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



"""
Exercise 1 (task 5 of 7):

You are given the prices of a stock, in the form of an array of integers, prices. Let's say that prices[i] is the price of the 
stock on the ith day (0-based index). Assuming that you are allowed to buy and sell the stock only once, your task is to find 
the maximum possible profit (the difference between the buy and sell prices).

* Notes: 
    - You can assume there are no fees associated with buying or selling the stock.

* Examples:

    For prices = [6, 3, 1, 2, 5, 4], the output should be buyAndSellStock(prices) = 4.
    It would be most profitable to buy the stock on day 2 and sell it on day 4. 
    Thus, the maximum profit is prices[4] - prices[2] = 5 - 1 = 4.

    For prices = [8, 5, 3, 1], the output should be buyAndSellStock(prices) = 0.
    Since the value of the stock drops each day, there's no way to make a profit from selling it. 
    Hence, the maximum profit is 0.

    For prices = [3, 100, 1, 97], the output should be buyAndSellStock(prices) = 97.
    It would be most profitable to buy the stock on day 0 and sell it on day 1. 
    Thus, the maximum profit is prices[1] - prices[0] = 100 - 3 = 97.
"""

# minimum price for buying variable 
# profit variable

# iterate using i in range(1, len):
    # compare current price less miniumum buy is bigger than profit:
        # update profit to current price - min buy
    # if current price less than min buy
        # update min but to current price

def buyAndSellStock(prices):
    buy_min = prices[0]
    profit = 0

    for i in range(1, len(prices)):
        if prices[i] - buy_min > profit:
            profit = prices[i] - buy_min
        if prices[i] < buy_min:
            buy_min = prices[i]

    return profit


print(buyAndSellStock([8])) # expected: 0
print(buyAndSellStock([8, 9, 10])) # expected: 2 ==>> prices[2] - prices[0] => 10 - 8 = 2
print(buyAndSellStock([6, 3, 1, 2, 5, 4])) # expected: 4 ==>> prices[4] - prices[2] => 5 - 1 = 4
print(buyAndSellStock([8, 5, 3, 1])) # expected: 0 ==>> all sales at a loss so no profit
print(buyAndSellStock([3, 3, 3, 3, 3, 3])) # expected: 0 ==>> all same price
print(buyAndSellStock([4, 3, 3, 3, 3, 4])) # expected: 1 ==>> prices[5] - prices[1] => 4 - 3 = 1
print(buyAndSellStock([3, 100, 1, 97])) # expected: 97 ==>> prices[1] - prices[0] => 4 - 3 = 1




"""
Exercise 2 (task 6 of 7):

Given a string, your task is to replace each of its characters by the next one in the English alphabet; 
i.e. replace 'a' with 'b', replace 'b' with 'c', etc ('z' would be replaced by 'a').

* Example:
    For inputString = "crazy", the output should be alphabeticShift(inputString) = "dsbaz"
"""

def alphabeticShift(input_string):
    result = ""

    for char in input_string:
        num = ord(char)

        # if letter is 'z' need to subtract to convert to 'a'
        if num == 122:
            num -= 26
        
        result += chr(num+1)

    return result


print(alphabeticShift("crazy")) # expected: dsbaz
print(alphabeticShift("z")) # expected: a
print(alphabeticShift("aaaabbbccd")) # expected: bbbbcccdde
print(alphabeticShift("fuzzy")) # expected: gvaaz
print(alphabeticShift("codesignal")) # expected: dpeftjhobm