class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        res = 0
        bob,me = 0, len(piles) - 2
        while bob < me:
            res += piles[me]
            bob += 1
            me -= 2
        return res