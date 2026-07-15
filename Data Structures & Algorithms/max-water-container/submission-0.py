"""
UMPIRE-

Understand - 
1. Input: integer array heights 
2. Output: integer that is maximum amount of water a container can store 

Map - 
two pointer approach? 

Implement- 
1. initialize max_vol 


"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_vol = 0 
        left = 0
        right = len(heights) - 1 
        while left< right:
            vol = min(heights[left], heights[right]) * (right-left)
            if vol > max_vol:
                max_vol = vol 
            if heights[left] < heights[right]:
                left = left + 1 
            else:
                right = right - 1 
        return max_vol
        