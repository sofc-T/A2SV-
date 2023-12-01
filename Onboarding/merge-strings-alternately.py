class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l , r= 0, 0
        ans = ""
        while l < len(word1) and r < len(word2):
            ans += word1[l] + word2[r]
            l += 1
            r += 1
        if l == len(word1)  and r != len(word2):
            ans += word2[r:]
        elif l != len(word1)  and r == len(word2):
            ans += word1[l:]
        return ans