class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open, close = 0 , 0
        for chr in s:
            if chr == "(":
                open += 1
            else:
                if not open:
                    close += 1
                else:
                    open -=  1
        return open + close