"""
UMPIRE 

Understand - 
1. Input - string containing only uppercase letters, integer k 
2. Output - int (length of the longest increasinf subsequence after replcing k characters)

Map - 

Plan - 
1. l = 0 r = 0 
2. Initialize the freq map of 26 characters with default value 0
3. Initialize max 
4. run a while loop until r reaches the end:
    - look at the highest freq in freq map 
    - calculate 
    - determine if valid or not 
    - if valid, count the length and update max 
    - if not valid, update l and remove 1 from l's freq count
    r = r + 1 
    add r to freq map 

do i wanna subtitiue top ks that are closest to most frequent appearing character in a window? 

window size = 10 
top feq = 4
k = 5 

"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0 
        max_length = 0 
        freq_map = {}

        for char in s:
            freq_map[char] = 0
        freq_map[s[0]] = 1

        while r < len(s):
            max_freq = max(freq_map.values())
            isValid = ((r-l+1) - max_freq) <= k
            if isValid:
                max_length = (r-l+1)
            else:
                freq_map[s[l]] -= 1 
                l += 1 
            r += 1
            if r < len(s):
                freq_map[s[r]] += 1  
        return max_length 
            
            



            

        