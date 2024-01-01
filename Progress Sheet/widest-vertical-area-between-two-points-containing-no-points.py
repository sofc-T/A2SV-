class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        maxx = 0
        xs = list(set([x[0] for  x in points]))
        xs.sort()
        for i in range(1,len(xs)):
            maxx = max(xs[i]-xs[i-1],maxx)
        return maxx