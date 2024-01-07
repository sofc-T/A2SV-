class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        vowels = {"a","e","i","o","u"}
        vows = 0
        for i in range(k):
            if s[i] in vowels:
                vows += 1
        l, r = 0, k
        # print(l,r,vows)
        curr = vows
        while r < len(s):
            # print(l,r,vows)
            if s[r] in vowels:
                curr += 1
            if s[l] in vowels:
                curr -= 1
            l+= 1
            r += 1
            vows = max(vows,curr)
        # print(curr,l,r)
        return vows