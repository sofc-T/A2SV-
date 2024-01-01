class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key = lambda p:(p[0]**2 + p[1]**2)**(0.5))
        return points[:k]