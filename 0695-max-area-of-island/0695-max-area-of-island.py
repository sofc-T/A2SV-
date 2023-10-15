class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxi = 0    
        
        def explore(row,col):
            nonlocal maxi
            if row < 0 or col < 0 or row >= rows or col >= cols:
                return 0

            if grid[row][col] == -1:
                return 0

            if grid[row][col] == 0:
                return 0
            grid[row][col] = -1
            tot = 1+ explore(row+1,col) + explore(row-1, col) + explore(row,col-1) + explore(row, col+1)
            maxi = max(maxi, tot)
            return tot

        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    explore(row,col)
        return maxi  