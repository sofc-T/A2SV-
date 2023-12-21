class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        maxxSum = 0
        for r in range(len(grid) - 2):
            c = 0
            while c < len(grid[0]) - 2:
                currSum = sum(grid[r][c:c+3])
                currSum += grid[r+1][c+1]
                currSum += sum(grid[r+2][c:c+3])
                maxxSum = max(maxxSum,currSum)
                c += 1
        return maxxSum