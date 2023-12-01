class Solution:
    def freqAlphabets(self, s: str) -> str:
        minn, res = ord("a") - 1, ""
        i = 0
        while i < len(s):
            if i < len(s) - 2 and s[i+2] == "#":
                val = int(s[i:i+2])
                res += chr(minn+int(s[i:i+2]))
                i += 3
            else:
                res += chr(minn+int(s[i]))
                i += 1
        return res