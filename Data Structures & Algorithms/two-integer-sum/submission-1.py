"""
Understand
Input: array of interegers and integer target
Output: pair of index in the form of a list 

Map: hashmap

Plan: 
1. put each index, value pair in a hashmap 
2. loop through nums and see if target - nums[i] exists in hashmap (O(1)) search
return index of i and index of value in hasmap as a list 

Implement:

"""



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashm = {}
        for i in range(len(nums)):
            hashm[nums[i]] = i
        for i in range(len(nums)):
            if (target - nums[i]) in hashm and (i != hashm.get((target - nums[i]))):
                return [i, hashm.get((target - nums[i]))]
        return None
        