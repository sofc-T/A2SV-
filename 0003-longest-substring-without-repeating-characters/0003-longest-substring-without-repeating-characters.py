class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = {}
        l, maxx = 0, 0
        for r in range(len(s)):
            char = s[r]
            if char in seen and seen[char] >= l:
                l = seen[char] + 1
            else:
                maxx = max(maxx,r-l+1) 
            seen[char] = r 
        return maxx