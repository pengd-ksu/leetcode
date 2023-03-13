class Solution:
    def isMatch(s, p):
        if not p:
            return not s
        
        first_match = bool(s) and p[0] in {s[0], '.'}

        if len(p) >= 2 and p[1] == '*':
            return (first_match and Solution.isMatch(s[1:], p)) or Solution.isMatch(s, p[2:])
        else:
            return first_match and Solution.isMatch(s[1:], p[1:])

    def isMatch_2(self, s: str, p: str) -> bool:
        #First two conditions could be combined.
        if not s and not p:
            return True
        elif s and not p:
            return False
        #This condition is the same as if len(p) > 1 and p[1] == '*' -> self.isMatch(s, p[2:])
        elif not s and p:
            if len(p) > 1 and p[1] == '*':
                return self.isMatch(s, p[2:])
        firstMatch = bool(s) and p[0] in {s[0], '.'}
        if len(p) > 1 and p[1] == '*':
            return (firstMatch and self.isMatch(s[1:], p)) or (self.isMatch(s, p[2:]))
        else:
            return firstMatch and self.isMatch(s[1:], p[1:])

    def isMatch_3(self, s: str, p: str) -> bool:
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(p):
                    ans = (i == len(s))
                else:
                    firstMatch = i <len(s) and p[j] in {s[i], '.'}
                    if j + 1 < len(p) and p[j + 1] == '*':
                        ans = dp(i, j + 2) or firstMatch and dp(i + 1, j)
                    else:
                        ans = firstMatch and dp(i + 1, j + 1)
                memo[i, j] = ans
            return memo[i, j]
        
        return dp(0, 0)

    def isMatch_4(self, text: str, pattern: str) -> bool:
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]

        return dp[0][0]

if __name__ == '__main__':
    print(Solution.isMatch(s="aaa", p="a*a"))