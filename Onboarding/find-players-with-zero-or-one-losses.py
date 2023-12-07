class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner, loser = {}, {}
        res = [[],[]]
        for w, l in matches:
            winner[w] = winner.get(w,0) + 1
            loser[l] = loser.get(l,0) + 1
        res[0] = sorted([num for num in winner if loser.get(num,0) == 0])
        res[1] = sorted([num for num in loser if loser[num] == 1])
        return res