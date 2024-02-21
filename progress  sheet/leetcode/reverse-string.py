class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0 , len(s) - 1
        def xo(l,r,s):
            if l >= r: return s
            s[l], s[r] = s[r], s[l]
            return xo(l+1, r-1, s)
        return xo(l,r,s)