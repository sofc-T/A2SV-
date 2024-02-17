class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        for idx in range(len(palindrome)//2):
            if palindrome[idx] != "a":
                return palindrome[:idx] + "a" + palindrome[idx+1:]
        return palindrome[:-1]+ "b"