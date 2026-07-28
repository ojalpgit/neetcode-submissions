"""
UMPIRE 

Understand - 
1. Input: string s 
2. Output: boolean 

Match - 
Stack 

Plan - 
1. Initialize two stacks 
2. in a for loop - 
    - add opening and closing chars to respective stacks 
3. if the length of both stacks not equal: 
    -return false 
4. pop each element in both the stacks and compare and return accordingly 
5. if both stacks empty, then return true 

"""
from collections import deque 
class Solution:
    def isValid(self, s: str) -> bool:
        open_stack = deque()
        for char in s:
            if char == "(" or char == "{" or char == "[":
                open_stack.append(char)
            else:
                if not open_stack:
                    return False
                o = open_stack.pop()
                if (o == '[' and char != ']') or (o == '{' and char != '}') or (o == '(' and char != ')'):
                    print("this false")
                    return False 
        if not open_stack:
            return True
        return False

        