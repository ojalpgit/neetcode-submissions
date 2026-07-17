"""
UMPIRE 

Understand - 
1. Input: string s 
2. Output: integer 

Map - Hashmap 

Plan - 
1. define max_length 
2. for loop
    - define a new hashmap 
    - add the ith element to hashmap 
    - check if subsequent elements belong to hashmap already 
        if they do, stop the while loop 
    - update max_length variable 
3. return max_length 
    
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        max_length = 0
        for i in range(len(s)):
            count = 0
            j = i 
            char_map = {}
            while j < len(s) and (s[j] not in char_map):
                count = count + 1 
                char_map[s[j]] = 0 
                j = j + 1
            if count > max_length: 
                max_length = count 
        return max_length 
        """
        charSet = set()
        l = 0 
        res = 0 

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l = l + 1 
            charSet.add(s[r])
            res = max(res, r-l+1)
        return res 



        
            



        