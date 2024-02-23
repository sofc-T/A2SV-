class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rows, cols = [] , []
        for r in grid:
            rows.append(max(r))
        for c in range(len(grid[0])):
            maxx = -1 * inf
            for r in range(len(grid)):
                maxx = max(grid[r][c],maxx)
            cols.append(maxx)
        total = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                total += min(rows[r],cols[c]) - grid[r][c]
        return total