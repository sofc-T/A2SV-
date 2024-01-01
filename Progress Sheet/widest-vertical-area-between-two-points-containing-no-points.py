class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points = sorted([x[0] for x in points])
        return max(points[i] - points[i-1] for i in range(len(points)))