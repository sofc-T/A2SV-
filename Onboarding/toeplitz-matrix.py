class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if len(matrix[0]) == 1:
            return True
        check_vals = matrix[0][:-1]
        for i in range(1,len(matrix)):
            if matrix[i][1:] == check_vals:
                pass
            else:
                return False
            check_vals = [matrix[i][0]] + check_vals[:-1]
        return True