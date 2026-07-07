class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for i in nums:
            if i in map:
                map[i] = map[i] + 1
            else:
                map[i] = 1
        for key, values in map.items():
            if map[key] >= 2:
                return True

        return False

        