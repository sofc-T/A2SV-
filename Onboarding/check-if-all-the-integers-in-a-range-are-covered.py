class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()
        points = [0] * 51
        for s, e in ranges:
            for ind in range(s,e+1):
                points[ind] = 1
        for ind in range(left,right+1):
            if points[ind] == 0:
                return False
        return True