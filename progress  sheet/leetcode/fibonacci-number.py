class Solution:
    def fib(self, n: int) -> int:
        def xo(n):
            return n if n < 2 else xo(n-1) + xo(n-2)
        return xo(n)