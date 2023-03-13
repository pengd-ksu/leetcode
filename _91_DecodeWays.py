from typing import List

from pytest import mark

class Solution:
    def numDecodings_brute(s: str) -> int:
        dp = [0] * len(s)
        if int(s[0]) == 0:
            return 0
        dp[0] = 1
        for i in range(1, len(dp)):
            if s[i] != '0':
                dp[i] = dp[i-1]
                if i >= 2 and s[i-1] != '0' and 0 < int(s[i-1:i+1]) < 27:
                    dp[i] += dp[i-2]
                elif i >= 1 and s[i-1] != '0' and 0 < int(s[i-1:i+1]) < 27:
                    dp[i] += 1
            else:
                if s[i-1] == '1' or s[i-1] == '2':
                    if i >= 2:
                        if 10 < int(s[i-2:i]) < 27:
                            dp[i] = dp[i-2]
                        else:
                            dp[i] = dp[i-1]
                    else:
                        dp[i] = dp[i-1]
                else:
                    return 0
        #print(dp)
        return dp[-1]

    def numDecodings_dp(s: str) -> int:
        if s[0] == '0':
            return 0

        n = len(s)
        dp = [0] * (n + 2)
        dp[n] = 1
        for i in range(n - 1, -1, -1):
            dp[i] += dp[i+1] if s[i] != '0' else 0
            dp[i] += dp [i+2] if 10 <= int(s[i:i+2]) <= 26 else 0
        #print(dp)
        return dp[0]

@mark.parametrize('s, expected', [
        ('12', 2),
        ('226', 3),
        ('0', 0),
        ('06', 0)
    ])

def test_numDecodings(s, expected):
    ans_brute = Solution.numDecodings_dp(s)
    assert ans_brute == expected