from typing import List

from pytest import mark
import unittest

import math

class Solution:
    def uniquePaths_math(m: int, n: int) -> int:
        #suppose we have one path, then the numerator would be the total
        #permutation of the path. However, we could only proceed from
        #left to right, and from top to bottom. The denominator indicate
        #the impossible movement in horizontal and vertical directions.
        return int(math.factorial(m-1+n-1) / (math.factorial(m-1) * math.factorial(n-1)))

    def uniquePaths_dp(self, m: int, n: int) -> int:
        # The robot could only move down or move right. The first column
        # and first row is a special case, only one way for each, so
        # initialize one. Initial corner is als set as 1, for the edge
        # case that there's only one row and one column in the matrix.
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

@mark.parametrize('rows, cols, expected',[
    (3, 7,28),
    (3, 2, 3),
])

def test_spiralOrder(rows, cols, expected):
    ans_math = Solution.uniquePaths_math(rows, cols)
    ans_dp = Solution.uniquePaths_dp(rows, cols)
    assert ans_math == expected
    assert ans_dp == expected