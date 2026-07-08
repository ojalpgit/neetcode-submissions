"""
UMPIRE 

Understand 
1. Input - array of integer nums 
2. Output - array of integer 

Map - lists 

Plan 
1. Initialize prefix and postfix list 
2. for loop
    - start with 1 
    - multiply prefix[i-1]*nums[i] to get prefix[i]
3. while i >= 0
    - start with 1
    - suffix[0] * nums[i] to get suffix[0]
4. for loop:
    -res[i] = suffix[i] * prefix[i]
5. return res
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1]*nums[i-1]
        i = len(nums)-2
        while i>=0:
            suffix_num = suffix[0] * nums[i+1]
            suffix.insert(0, suffix_num)
            i = i - 1 
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = prefix[i] * suffix[i]
        return res


        


        