"""
UMPIRE- 

Understand- 
1. Input: array of integers that is sorted in ascending order 
2. Output: list of index [index1, index2] index1 < index2 st numbers[index1] + numbers[index2] == target(1-indexed)

Map- 
Two pointer approach 

Plan- 
1. define left and right pointers 
2. while left<right:
    - calculate nums[left] + nums[right]
    if this > target:
        right = right -1 
    elif this < target:
        left = left + 1 
    else:
        return [left+1, right+1]
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 0 or len(numbers) == 1:
            return []
        left = 0
        right = len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum > target:
                right = right - 1
            elif sum < target:
                left = left + 1 
            else: 
                return [left+1, right+1]
        return []
        