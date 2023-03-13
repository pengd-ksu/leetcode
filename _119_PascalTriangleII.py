from typing import List
from pytest import mark

class Solution:
    def getRow(rowIndex: int) -> List[int]:
        dp = [[1 for _ in range(i + 1)] for i in range(rowIndex + 1)]
        #dp[0]=[1], dp[1]=[1,1], dp[2]=[1,1,1],etc...
        for i in range(2, rowIndex + 1):
            for j in range(1, i):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        return dp[rowIndex]

@mark.parametrize('rowIndex, expected', [
        (3, [1,3,3,1]),
        (0, [1]),
        (1, [1,1]),
    ])

def test_getRow(rowIndex, expected):
    ans = Solution.getRow(rowIndex)
    assert ans == expected