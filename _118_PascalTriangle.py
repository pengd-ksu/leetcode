from typing import List
from pytest import mark

class Solution:
    def generate(numRows: int) -> List[List[int]]:
        dp = [[1 for _ in range(i)] for i in range(numRows + 1)]
        
        for i in range(1, numRows + 1):
            if i >= 3:#dp[0] = [], dp[1] == [1], dp[2] == [1,1]
                for j in range(1, i - 1):
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                    
        return dp[1:]#because dp[0] = []

    def generate_mirror(numRows: int) -> List[List[int]]:
        dp = [[1 for _ in range(i)] for i in range(numRows + 1)]
        
        for i in range(1, numRows + 1):
            if i >= 3:#dp[0] = [], dp[1] == [1], dp[2] == [1,1]
                for j in range(1, i // 2 + 1):#mirror
                    dp[i][j] = dp[i][-j - 1] = dp[i - 1][j - 1] + dp[i - 1][j]
                    
        return dp[1:]#because dp[0] = []

@mark.parametrize('numRows, expected', [
        (5, [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]),
        (1, [[1]]),
    ])

def test_generate_mirror(numRows, expected):
    ans_mirror = Solution.generate_mirror(numRows)
    assert ans_mirror == expected