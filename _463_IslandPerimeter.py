class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        M, N, count = len(grid), len(grid[0]), 0
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == 1:
                    if m == 0 or grid[m-1][n] == 0:
                        count += 1
                    if m == M - 1 or grid[m+1][n] == 0:
                        count += 1
                    if n == 0 or grid[m][n-1] == 0:
                        count += 1
                    if n == N - 1 or grid[m][n+1] == 0:
                        count += 1
        return count