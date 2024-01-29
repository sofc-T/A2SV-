class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        for r in range(len(matrix)):
            total = 0
            for c in range(len(self.matrix[0])):
                total += self.matrix[r][c]
                self.matrix[r][c] = total
        for c in range(len(self.matrix[0])):
            total = 0
            for r in range(len(self.matrix)):    
                total += self.matrix[r][c]
                self.matrix[r][c] = total
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        val = self.matrix[row2][col2] 
        if row1 > 0 and col1 > 0:
            val += self.matrix[row1-1][col1-1] - self.matrix[row2][col1-1] - self.matrix[row1-1][col2]
        elif row1 > 0:
            val -= self.matrix[row1-1][col2]
        elif col1 > 0:
            val -= self.matrix[row2][col1-1]
        return val

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)