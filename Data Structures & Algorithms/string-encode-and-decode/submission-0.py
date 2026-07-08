class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            length = len(s)
            len_of_len = len(str(length))
            for i in range(4-len_of_len):
                res = res + str(0)
            res = res + str(length)
            res = res + s
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            length = int(s[i:i+4])
            sub_str = s[i+4: i+4+length]
            res.append(sub_str)
            i = i + 4 + length 
        return res


