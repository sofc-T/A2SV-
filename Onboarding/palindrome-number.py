class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = 0
        temp = x + 1 -1
        limit = 1 * 10 ** (len(str(x)) - 1)
        while limit >= 1:
            # print(reverse,mul,limit)
            reverse += (x % 10) * limit
            limit //= 10
            x //= 10
        return reverse == temp
            
