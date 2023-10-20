class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        start = None
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                    break
            if start:
                break

        q = [start]
        grid[i][j] = 2
        while q:
            i, j = q.pop(0)
            for r, c in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if not (0 <= r < n and 0 <= c < n):
                    continue
                if grid[r][c] in (0, 2):
                    continue
                q.append((r, c))
                grid[r][c] = 2

        q = [(i, j, 0) for i in range(n) for j in range(n) if grid[i][j] == 2]
        while q:
            i, j, d = q.pop(0)
            for r, c in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if not (0 <= r < n and 0 <= c < n):
                    continue
                if grid[r][c] == 2:
                    continue
                if grid[r][c] == 1:
                    return d
                q.append((r, c, d+1))
                grid[r][c] = 2
        return None