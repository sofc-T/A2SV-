class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        seenAt = {}
        minLen = inf
        for i, num in enumerate(cards):
            if num in seenAt:
                minLen = min(minLen,i-seenAt[num] + 1)
                seenAt[num] = i
            else:
                seenAt[num] = i
        return minLen if minLen != inf else -1