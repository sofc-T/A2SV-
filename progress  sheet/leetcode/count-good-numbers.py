class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # return ((4 ** (n//2)) * (5 ** ceil(n/2))) % (10**9 + 7)
        def xo(n,x):
            if x == 0: return 1
            if n == 0: return 0
        
            if x % 2: return xo(n% (10**9 + 7),x-1)  * n
            return xo(n*n% (10**9 + 7),x//2)
        return (xo(4,n//2)  * xo(5,ceil(n/2)))  % (10**9 + 7)


        