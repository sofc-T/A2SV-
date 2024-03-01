class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def xo(n):
            return n == 1 if n <= 1 else xo(n/4)    
        return xo(n)