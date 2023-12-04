class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1=  0
        base = ord("0")
        for val in num1:
            n1 *= 10
            n1 += ord(val) - base
        n2 = 0
        for val in num2:
            n2 *= 10
            n2 += ord(val) - base
        return str(n1 * n2)