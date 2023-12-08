class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        space = set(spaces)
        ans = ""
        for ind in range(len(s)):
            if ind in space:
                ans += " "
                ans += s[ind]
            else:
                ans += s[ind]
        return ans