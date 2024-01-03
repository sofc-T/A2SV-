class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s) - 1
        while l < r:
            if ord(s[l]) not in range(65,91)  and ord(s[l]) not in range(97,123) and ord(s[l]) not in range(48,58):
                l += 1
            elif ord(s[r]) not in range(65,91)  and ord(s[r]) not in range(97,123) and ord(s[r]) not in range(48,58):
                r -= 1
            elif s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True