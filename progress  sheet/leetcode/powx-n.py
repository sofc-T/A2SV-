class Solution:
    def myPow(self, n: float, x: int) -> float:
        def xo(n,x):
            if x == 0: return 1
            if n == 0: return 0
        
            if x % 2: return xo(n,x-1) * n
            return xo(n*n,x//2)
        return xo(n,x) if x >= 0 else 1/xo(n,abs(x))