from typing import List

from pytest import mark
import unittest

class Solution:
    def climbStairs(n: int) -> int:
        dp = [0] * (n + 1)
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:#n >= 3
            dp[1], dp[2] = 1, 2
            for k in range(3, n + 1):
                dp[k] = dp[k - 2] + dp[k - 1]
        return dp[n]
    #2 steps before, jump 2 steps here; 1 step before, jump 1 step

    def climbStairs_2(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[0], dp[1] = 1, 1 # dp[0] set to 1 for dp[2], 2 steps from dp[0] to dp[2]
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

@mark.parametrize('n, expected',[
    (2, 2),
    (3, 3),
    (4, 5),
])

def test_climbStairs(n, expected):
    ans = Solution.climbStairs(n)
    assert ans == expected