class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        amount = 0
        diff = []
        for a , b in costs:
            diff.append(a-b)
            amount += b
        diff.sort()
        for i in range(len(costs)//2):
            amount += diff[i]
        return amount