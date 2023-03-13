from typing import List

from pytest import mark
import unittest

class Solution:
    def minPathSum(grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        #grid stores minimum path to it from left or top
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    grid[i][j] = grid[i][j]
                elif i == 0:
                    grid[i][j] = grid[i][j] + grid[i][j-1]
                elif j == 0:
                    grid[i][j] = grid[i][j] + grid[i-1][j]
                else:
                    grid[i][j] = grid[i][j] + min(grid[i-1][j], grid[i][j-1])
        print(grid)
        return grid[-1][-1]

    def minPathSum_2(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [row[:] for row in grid]
        for i in range(m):
            for j in range(n):
                if i == 0 and j > 0:
                    dp[i][j] += dp[i][j-1]
                elif i > 0 and j == 0:
                    dp[i][j] += dp[i-1][j]
                elif i > 0 and j > 0:
                    dp[i][j] += min(dp[i-1][j], dp[i][j-1])
        return dp[m-1][n-1]

@mark.parametrize('grid, expected',[
    ([[1,3,1],[1,5,1],[4,2,1]], 7),
    ([[1,2,3],[4,5,6]], 12),
])

def test_spiralOrder(grid, expected):
    ans = Solution.minPathSum(grid)
    assert ans == expected