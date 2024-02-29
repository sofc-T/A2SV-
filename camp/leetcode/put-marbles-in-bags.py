class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == len(weights):
            return 0
        if k == 1:
            return 0
        vals = []
        for idx in range(len(weights)-1):
            vals.append(weights[idx] + weights[idx+1])
        vals.sort()
        return sum(vals[-1*(k-1):]) - sum(vals[:k-1])
