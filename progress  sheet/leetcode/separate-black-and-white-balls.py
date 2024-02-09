class Solution:
    def minimumSteps(self, s: str) -> int:
        l, r = 0 , 0
        count, s = 0, list(s)
        while l < len(s) and r  < len(s):
            if s[l] == "0":
                l += 1
                r += 1
            elif s[r] == "0":
                count += r - l
                s[l], s[r] = s[r], s[l]
                l += 1
                r += 1
            else:
                r += 1
        return count