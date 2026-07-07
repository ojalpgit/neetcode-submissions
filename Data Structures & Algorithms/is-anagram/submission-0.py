class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_map_s = {}
        for char in s:
            if char in freq_map_s:
                freq_map_s[char] = freq_map_s.get(char) + 1
            else:
                freq_map_s[char] = 1
        freq_map_t = {}
        for char in t:
            if char in freq_map_t:
                freq_map_t[char] = freq_map_t.get(char) + 1
            else:
                freq_map_t[char] = 1
        
        return freq_map_s == freq_map_t