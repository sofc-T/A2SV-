class Solution:
    def balancedString(self, s: str) -> int:
        count = {"W":0,"Q":0,"E":0,"R":0}
        correction, invalids = 0, set()
        occurence, valid = Counter(s), len(s) // 4
        for chr in occurence:
            if occurence[chr] > valid:
                count[chr] = occurence[chr] - valid
                correction += occurence[chr] - valid
                invalids.add(chr)
        
        if correction == 0:
            return 0
        corrected, minLen = 0, inf
        l, r = 0 , 0
        while r < len(s):
            if s[r] in invalids:
                corrected += 1
                count[s[r]] -= 1
            while corrected >= correction and max(count.values())<= 0:
                minLen = min(minLen,r-l+1)
                if s[l] in invalids:
                    count[s[l]] += 1
                    corrected -= 1
                l += 1
            r += 1
        return minLen