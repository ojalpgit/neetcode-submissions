"""
UMPIRE 

Understand - 
1. Input: array of integers height 
2. Output: maximum area of water 

Map - 


5


"""

class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height)
        suffix = [0] * len(height)
        
        prefix[0] = height[0]
        for i in range(1, len(height)):
            if prefix[i-1] > height[i]:
                prefix[i] = prefix[i-1]
            else:
                prefix[i] = height[i]

        suffix[len(height)-1] = height[-1]
        i = len(height) - 2
        while i >= 0:
            if suffix[i+1] > height[i]:
                suffix[i] = suffix[i+1]
            else:
                suffix[i] = height[i]
            i = i-1 
        max_vol = 0
        for i in range(len(height)):
            single_vol = min(prefix[i], suffix[i]) - height[i]
            print(single_vol)
            max_vol = max_vol + single_vol
        return max_vol 




        

        