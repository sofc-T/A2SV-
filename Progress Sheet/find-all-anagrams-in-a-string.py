class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        pCounter = Counter(p)
        l,r = 0, len(p)
        ans = []
        sCounter = Counter(s[:r])
        if sCounter == pCounter and len(s) == len(p):
            return [0]
        while r < len(s):
            if sCounter == pCounter:
                ans.append(l)
            sCounter[s[l]] -= 1 
            l += 1
            if sCounter[s[r]] > -1:
                sCounter[s[r]] += 1  
            else:
                sCounter[s[r]] = 1
            r += 1
        if sCounter == pCounter:
            ans.append(l)
        return ans