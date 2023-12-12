class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        good = inf
        sames = set()
        for ind in range(len(backs)):
            if fronts[ind] == backs[ind]:
                sames.add(fronts[ind])
        for ind in range(len(backs)):
            if fronts[ind] not in sames:
                good = min(good,fronts[ind])
            if backs[ind] not in sames:
                good = min(good,backs[ind])
        return good if good != inf else 0