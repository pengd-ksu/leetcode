class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        dp = [[0 for _ in range(n)] for _ in range(n)]
        idx = 0
        while idx < n:
            dp[idx][idx] = 1
            idx += 1
            ans += 1
        for col in range(1, n):
            for row in range(col):
                if row == col - 1 and s[row] == s[col]:
                    dp[row][col] = 1
                    ans += 1
                elif dp[row+1][col-1] == 1 and s[row] == s[col]:
                    dp[row][col] = 1
                    ans += 1
        return ans

    def countSubstrings_2(self, s: str) -> int:
        L, r = len(s), 0
        for i in range(L):
            for a,b in [(i,i),(i,i+1)]:
                while a >= 0 and b < L and s[a] == s[b]: a -= 1; b += 1
                r += (b-a)//2
        return r