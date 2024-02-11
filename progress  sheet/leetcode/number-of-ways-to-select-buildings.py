class Solution:
    def numberOfWays(self, s: str) -> int:
        count = Counter(s)
        zeroesBefore, onesBefore = 0 , 0
        result = 0
        for chr in s:
            if chr == "1":
                result += zeroesBefore * (count["0"] - zeroesBefore)
                onesBefore  += 1
            else:
                result += onesBefore * (count["1"] - onesBefore)
                zeroesBefore += 1
        return result
