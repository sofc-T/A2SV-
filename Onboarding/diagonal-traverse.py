class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        r, c = len(mat), len(mat[0])
        row, col = 0, 0
        
        while len(res) < r * c:
            while row > -1 and col < c:
                res.append(mat[row][col])
                row -= 1
                col += 1

            if col >= c: 
                col = c - 1
                row += 2
            if row < 0: row = 0

            while col > -1 and row < r:
                res.append(mat[row][col])
                row += 1
                col -= 1
            if row >= r: 
                row = r- 1
                col += 2
            if col < 0: col = 0

        return res