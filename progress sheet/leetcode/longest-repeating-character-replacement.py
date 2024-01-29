class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l, r = 0, 0
        moves = 0
        while r < len(s):
            count[s[r]] = count.get(s[r],0) + 1
            moves = max(moves,count[s[r]])
            if r - l+ 1 > moves + k:
                count[s[l]] -= 1
                l += 1
            r += 1
        return r - l 
            