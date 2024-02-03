class Solution:
    def maxScore(self, s: str) -> int:
        ones = 0
        for chr in s:
            ones += int(chr)
        idx = 0
        maxx = 0
        left , right = 0 , ones
        while idx < len(s) - 1:
            if s[idx] == "0":
                left += 1
            else:
                right -= 1
            maxx = max(left+right,maxx)
            # print(left,right)
            idx += 1
        return maxx