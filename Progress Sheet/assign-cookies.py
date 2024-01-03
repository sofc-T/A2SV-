class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i1, i2 = 0, 0
        while i1 < len(g) and i2 < len(s):
            if s[i2] >= g[i1]:
                i1 += 1
                i2 += 1
            else:
                i2 += 1
        return i1