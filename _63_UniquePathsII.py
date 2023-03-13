class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    dp[i][j] = 1
                elif obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 0
        return dp[m-1][n-1]

    def uniquePathsWithObstacles_2(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        for i in range(m):
            for j in range(n):
                if i == 0 and j > 0:
                    dp[i][j] = dp[i][j-1] if obstacleGrid[i][j] == 0 else 0
                elif i > 0 and j == 0:
                    dp[i][j] = dp[i-1][j] if obstacleGrid[i][j] == 0 else 0
                elif i > 0 and j > 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1] if obstacleGrid[i][j] == 0 else 0
        return dp[m-1][n-1]

    def uniquePathsWithObstacles_dfs(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        @lru_cache(maxsize = None)
        def dfs(i: int, j: int):
            if obstacleGrid[i][j]:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            count = 0
            if i < m - 1:
                count += dfs(i+1, j)
            if j < n - 1:
                count += dfs(i, j+1)
            return count
        
        return dfs(0, 0)