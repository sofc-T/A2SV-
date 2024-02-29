class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        queue = deque(list(range(len(deck)-1,-1,-1)))
        deck.sort()
        curr, ans = 0, [0] * len(deck)
        while queue:
            ans[queue.pop()] = deck[curr]
            curr += 1
            if queue:
                queue.appendleft(queue.pop())
        return ans
        