class Solution:
    def isPalindrome(self, s: str) -> bool:
        val = ""
        for char in s:
            if char.isalnum():
                val += char.lower()
        return val == val[::-1]