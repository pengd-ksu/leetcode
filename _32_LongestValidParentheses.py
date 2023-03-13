class Solution:
    def longestValidParentheses(self, s: str) -> int:
        longest = 0
        dp =[0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = dp[i-2] + 2 if i >= 2 else 2
                # s[i-1] == ')'. If s[i] could be valid, then s[i-1] must
                # be valid too. Therefore, s[i-dp[i-1]-1] must be a '('
                else:
                    if i - dp[i-1] - 1 >= 0 and s[i-dp[i-1]-1] == '(':
                        dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2] if i - dp[i-1]-2 >= 0 else dp[i-1] + 2
                longest = max(longest, dp[i])
        return longest