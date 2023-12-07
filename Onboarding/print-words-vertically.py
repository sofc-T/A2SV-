class Solution:
    def printVertically(self, s: str) -> List[str]:
        max_length = 0
        res = []
        s = s.split()
        for word in s:
            max_length = max(max_length, len(word))
        res = [""] * max_length
        for ind in range(max_length):
            for word in s:
                if ind >= len(word):
                    val = " "
                else:
                    val = word[ind]
                res[ind] += val
        for ind in range(len(res)):
            res[ind] = res[ind].rstrip()
        return res