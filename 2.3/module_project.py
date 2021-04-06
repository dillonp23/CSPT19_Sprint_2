

"""
Sprint 2.3 - Stacks & Queues CodeSignal Assignment
"""



"""
Exercise 1: Queue on Stacks (Task 3 of 4)

Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
Implement a queue using two stacks.

You are given an array of requests, where requests[i] can be "push <x>" or "pop". Return an array composed of the results 
of each "pop" operation that is performed.

* Example:
    For requests = ["push 1", "push 2", "pop", "push 3", "pop"], the output should be
    queueOnStacks(requests) = [1, 2]

    After the first request, the queue is {1}; after the second it is {1, 2}. Then we do the third request, "pop", and add the 
    first element of the queue 1 to the answer array. The queue becomes {2}. After the fourth request, the queue is {2, 3}. Then 
    we perform "pop" again and add 2 to the answer array, and the queue becomes {3}.
"""

# UPER - Plan:
# def push(x):
    # elements always pushed into left stack

# def pop() -> int:
    # whenever pop is called, we need to see if the right stack is empty
    # if right stack isEmpty:
        # we need to pop all elements from left into right
        # while left is not empty:
            # ele = left.pop()
            # right.push(ele)

    # after filling right, or if right stack wasn't empty, we just return right.pop()
    # return right.pop()

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]


def queueOnStacks(requests):
    left = Stack()
    right = Stack()

    def insert(x):
        left.push(x)

    def remove():
        if right.isEmpty():
            while not left.isEmpty():
                ele = left.pop()
                right.push(ele)
            
        return right.pop()

    ans = []

    for request in requests:
        req = request.split(" ")
        
        if req[0] == 'push':
            insert(int(req[1]))
        else:
            ans.append(remove())


    return ans



print("Exercise 1: Queue on Stacks")
requests = ["push 1", "push 2", "pop", "push 3", "pop"]
expected = [1,2]
result = queueOnStacks(requests)
print(result) # expected: [1,2]
assert result == expected

requests = ["push 0", "pop"]
expected = [0]
result = queueOnStacks(requests)
print(result) # expected: [0]
assert result == expected


requests = ["push -6", "push -8", "push -9", "push 0", "push 9", "pop", "pop", "push 3", "pop", "pop", "pop", "pop"]
expected = [-6,-8,-9,0,9,3]
result = queueOnStacks(requests)
print(result) # expected: [-6,-8,-9,0,9,3]
assert result == expected

requests = ["push -539", "push -36", "pop", "push -312", "pop", "push 0", "push -910", "pop", "push 3", "pop", "pop"]
expected = [-539,-36,-312,0,-910]
result = queueOnStacks(requests)
print(result) # expected: [-539,-36,-312,0,-910]
assert result == expected




"""
Exercise 2: Valid Bracket Sequence (task 4 of 4)

Given a string sequence consisting of the characters '(', ')', '[', ']', '{', and '}'. Your task is to determine 
whether or not the sequence is a valid bracket sequence.

* Valid bracket sequence is defined in the following way:
    - an empty bracket sequence is a valid bracket sequence.
    - if S is a valid bracket sequence then (S), [S] and {S} are also valid.
    - if A and B are valid bracket sequences then AB is also valid.

* Examples:
    - sequence = "()", the output should be validBracketSequence(sequence) = true
    - sequence = "()[]{}", the output should be validBracketSequence(sequence) = true
    - sequence = "(]", the output should be validBracketSequence(sequence) = false
    - sequence = "([)]", the output should be validBracketSequence(sequence) = false
    - sequence = "{[]}", the output should be validBracketSequence(sequence) = true
"""

# UPER - Plan:
# initialize a new stack
# iterate through each character of string
# if character of string == ')' or ']' or '}':
    # if stack.peek() == inverse of character:
        # stack.pop()
    # else:
        # return False
# else (character is an open bracket):
    # stack.push(char)
# return stack.isEmpty()

def validBracketSequence(sequence):
    pass


# helper function to more easily check even brackets
def closedInverse(char):
    if char == ")":
        return "("
    elif char == "]":
        return "["
    elif char == "}":
        return "{"



print("\nExercise 2: Valid Bracket Sequence")
print(validBracketSequence("")) # expected: True
print(validBracketSequence("()")) # expected: True
print(validBracketSequence("][")) # expected: False
print(validBracketSequence("(]")) # expected: False
print(validBracketSequence("()[]{}")) # expected: True
print(validBracketSequence("{[]}")) # expected: True
print(validBracketSequence("([)]")) # expected: False
print(validBracketSequence("[[(({()}))]]{()}[({})]")) # expected: True