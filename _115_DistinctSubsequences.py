from pytest import mark

class Solution:
    def numDistinct_brute1(self, s: str, t: str) -> int:
    #not sure if the brute method is right or not
    times = 0
    def recursive(s, t):
        nonlocal times
        if len(s) < len(t):
            return
        if s[0] == t[0] and len(t) == 1:
            times += 1
            if len(s) > 1:
                return recursive(s[1:], t)#maybe more fits after this
            else:
                return
        elif s[0] == t[0]:
            recursive(s[1:], t[1:])
            recursive(s[1:], t)
        else:
            recursive(s[1:], t)
    recursive(s, t)
    return times

    def numDistinct_brute2(self, s: str, t: str) -> int:
        #Much faster than both dp. Drop many routes ealier, because of #1
        dp = {}
        def recursive(i, j):
            if len(s) - 1 - i < len(t) - j - 1:#1
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            if i == len(s) and j < len(t):
                return 0
            if j == len(t):
                return 1
            if s[i] == t[j]:
                dp[(i, j)] = recursive(i + 1, j + 1) + recursive(i + 1, j)
                return dp[(i, j)]
            else:
                dp[(i, j)] = recursive(i + 1, j)
                return dp[(i, j)]
        return recursive(0, 0)

    def numDistinct_dp(self, s: str, t: str) -> int:
        m, n = len(t), len(s)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for j in range(n + 1):
            dp[0][j] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[m][n]

    def numDistinct_dp_improve(self, s: str, t: str) -> int:
        m, n = len(t), len(s)
        dp = {}
        for j in range(n + 1):
            dp[(0, j)] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if t[i - 1] == s[j - 1]:
                    dp[(i, j)] = dp.get((i,j), 0) + dp.get((i,j), 0)dp[i][j - 1]
                else:
                    dp[(i, j)] = dp.get((i, j - 1), 0)
        return dp.get((m, n), 0)

    def numDistinct_dp2(self, s: str, t: str) -> int:
        n, m = len(s),len(t)
        dp = [0]*m 
        for i in range(n):
            prev = 1
            for j in range(m):
                if s[i] == t[j]:
                    prev, dp[j] = dp[j], prev + dp[j]
                else:
                    prev = dp[j]
        return dp[m-1]

#       ""  r  a  b  b  b  i  t
#    ""  1  1  1  1  1  1  1  1
#    r   0  1  1  1  1  1  1  1 
#    b   0  0  0  1  2  3  3  3
#    t   0  0  0  0  0  0  0  3