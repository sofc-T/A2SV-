class Solution:
    def reverseWords(self, s: str) -> str:
        ans = " "
        s = s.split()
        return ans.join(reversed(s))