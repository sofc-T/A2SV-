class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        l, r = 0, k
        s = list(s)
        while l < len(s):
            s[l:r] = s[l:r][::-1]
            l += 2*k
            r += 2*k
        return "".join(s)