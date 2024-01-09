class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r= 0, 0
        maxL = 0
        seen = {}
        while r < len(s):
            if s[r] not in seen:
                seen[s[r]] = r
                r += 1
            else:
                if seen[s[r]] >= l:
                    maxL = max(maxL, r- l)
                    l = seen[s[r]] + 1
                    seen[s[r]] = r 
                    r += 1
                else:
                    seen[s[r]] = r
                    r += 1
        return max(maxL,r-l)