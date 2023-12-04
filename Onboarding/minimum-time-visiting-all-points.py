class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        
        time = 0
        for i in range(len(points)-1):
            x, y = points[i]
            a, b = points[i+1]
            if abs(a-x) == abs(b-y):
                time += abs(a-x)
            else:
                f_d = min(abs(a-x),abs(b-y))
                time += f_d 
                time += max(abs(a-x),abs(b-y)) - f_d
        return time