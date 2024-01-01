class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        c, i = 0, 0
        while coins > 0 and i < len(costs):
            c += 1
            coins -= costs[i]
            i += 1
        if coins > -1: return c
        return c - 1