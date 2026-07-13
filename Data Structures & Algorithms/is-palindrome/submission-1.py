class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        for char in s:
            if char.isalnum():
                st = st + char.lower()
        print(st)
        return helper(st)

def helper(s):
        if len(s) == 0:
            return True
        if len(s) == 1:
            return True 
        if len(s) == 2:
            if s[0] == s[1]:
                return True
            else:
                return False
        if s[0] != s[len(s)-1]:
            return False
        return helper(s[1:len(s)-1])
        