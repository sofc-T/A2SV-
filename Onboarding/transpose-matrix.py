class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        c = len(matrix)
        res = []
        for i in range(len(matrix[0])):
            row = []
            for j in range(len(matrix)):
                row.append(matrix[j][i])
            res.append(row)
        return res
