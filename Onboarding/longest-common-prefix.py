class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        i = 0
        first = strs[0]
        last = strs[-1]
        while i < min(len(first),len(last)):
            if first[i] == last[i]:
                i += 1
            else:
                return first[:i]
        if len(first) < len(last):
            return first
        return last
