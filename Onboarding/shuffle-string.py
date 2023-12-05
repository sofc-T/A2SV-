class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [0] * len(s)
        for ind in range(len(indices)):
            res[indices[ind]] = s[ind]
        return "".join(res)