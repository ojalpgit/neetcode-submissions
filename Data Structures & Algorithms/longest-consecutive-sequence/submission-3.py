"""
UMPIRE- 

Understand- 
1. Input - array of integers "nums"
2. Output - length of the longest consecutive sequence 

Map - hashmap 

Plan - 
1. convert the array into a hashmap 
2. find the starting elements 
3. find the length of the subsequence from the starting element 

"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        nums_map = {}
        for i in nums:
            nums_map[i] = 0
        starts = []
        for i in nums:
            if i-1 not in nums_map:
                starts.append(i)
        max_length = 0
        for i in starts:
            j = i
            k = 0
            count = 1 
            while k < len(nums):
                if j + 1 in nums_map:
                    count = count + 1
                    j = j+1
                if count > max_length:
                    max_length = count 
                k = k+1 
        return max_length 
        """
        #optimal code after looking at the solution 
        numSet = set(nums)
        longest = 0 

        for i in numSet:
            if i-1 not in numSet:
                length = 0 
                while i+length in numSet:
                    length = length + 1 
                longest = max(length, longest)
        return longest
        

            

        