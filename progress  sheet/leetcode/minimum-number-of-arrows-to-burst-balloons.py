class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[1])
        arrows, upto = 0 , -1 * inf
        for xi , xf in points:
            if xi > upto:
                arrows += 1
                upto = xf
        return arrows