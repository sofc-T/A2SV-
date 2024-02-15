class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        length, odd = 0, False
        for val in count:
            if count[val] % 2:
                length += count[val] - 1
                odd = True
            else:
                length += count[val]
        return length + 1 if odd else length