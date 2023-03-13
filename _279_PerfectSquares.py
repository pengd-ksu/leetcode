class Solution:
    def numSquares(self, n: int) -> int:
        #The largest perfect square to n is int(n**0.5), and try less and less ones
        dp = [i for i in range(n + 1)]
        for i in range(n + 1):
            for j in range(1, int(i**0.5) + 1):
                dp[i] = min(dp[i], dp[i - j * j] + 1)
        return dp[n]