"""
UMPIRE- 

Understand- 
1. Input: array of integer nums 
2. Output: list of triplets (where each triplet is a list)

Map- 
1. Hashmap 

Plan- 
1. putting all of the values in a hashmap 
2. -nums[i] = nums[i] + nums[j] where -nums[i] is going to be my target 
3. solve via two pointer approach 

-4 -1 -1 0 1 2 
for i in 6:
    target = 1 
    left = 0
    right = 5

"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = set()
        for i in range(len(nums)):
            target = -nums[i]
            left = i + 1
            right = len(nums) -1 
            while left < right:
                sum = nums[left] + nums[right]
                if sum < target:
                    left = left + 1 
                elif sum > target:
                    right = right - 1 
                else:
                    res.add((nums[i], nums[left], nums[right]))
                    left = left + 1
        list_res = []
        for tup in res:
            list_res.append(list(tup))
        return list_res




        