from typing import List
from pytest import mark

class Solution:
    def isInterleave_brute(s1: str, s2: str, s3: str) -> bool:
        def Recur_Interleave(s1: str, i: int, s2: str, j: int, res: str, s3: str) -> bool:
            if res == s3 and i == len(s1) and j == len(s2):
                return True
            ans = False
            if i < len(s1):
                ans |= Recur_Interleave(s1, i + 1, s2, j, res + s1[i], s3)
            if j < len(s2):
                ans |= Recur_Interleave(s1, i, s2, j + 1, res + s2[j], s3)
            return ans
        
        if len(s1) + len(s2) != len(s3):
            return False
        return Recur_Interleave(s1, 0, s2, 0, '', s3)

    def isInterleave_memo(s1: str, s2: str, s3: str) -> bool:
        def Recur_Interleave_memo(s1: str, i: int, s2: str, j: int, s3: str, 
            k: int, memo: List[List[int]]) -> bool:
            if i == len(s1):
                return s2[j:] == s3[k:]
            if j == len(s2):
                return s1[i:] == s3[k:]
            if memo[i][j] >= 0:
                return True if memo[i][j] == 1 else False
            ans = False
            if ((s3[k] == s1[i] and Recur_Interleave_memo(s1, i + 1, s2, j, s3, k + 1, memo))
                or (s3[k] == s2[j] and Recur_Interleave_memo(s1, i, s2, j + 1, s3, k + 1, memo))):
                ans = True
            memo[i][j] = 1 if ans else 0
            return ans

        if len(s1) + len(s2) != len(s3):
            return False
        memo = [[-1 for _ in range(len(s2))] for _ in range(len(s1))]
        return Recur_Interleave_memo(s1, 0, s2, 0, s3, 0, memo)

    def isInterleave_memo_simple(s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        
        def helper(i, j, k):
            if (i, j) in seen:
                return False
            seen.add((i, j))
            if i == len(s1):
                return s2[j:] == s3[k:]
            if j == len(s2):
                return s1[i:] == s3[k:]
            if ((s1[i] == s3[k] and helper(i + 1, j, k + 1)) or
                    (s2[j] == s3[k] and helper(i, j + 1, k + 1))):
                return True
            return False

        seen = set()
        return helper(0, 0, 0)

    def isInterleave_memo_dp_2d(s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        
        dp = [[None for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = (dp[i][j - 1] and s2[j - 1] == s3[i + j -1])
                elif j == 0:
                    dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j -1])
                else:
                    dp[i][j] = ((dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]))

        return dp[len(s1)][len(s2)]

    def isInterleave_memo_dp_1d(s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        
        dp = [None for _ in range(len(s2) + 1)]
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == 0 and j == 0:
                    dp[j] = True
                elif i == 0:
                    dp[j] = (dp[j - 1] and s2[j - 1] == s3[i + j -1])
                elif j == 0:
                    dp[j] = (dp[j] and s1[i - 1] == s3[i + j -1])
                else:
                    dp[j] = ((dp[j] and s1[i - 1] == s3[i + j - 1])
                     or (dp[j - 1] and s2[j - 1] == s3[i + j - 1]))

        return dp[len(s2)]

@mark.parametrize('s1, s2, s3, expected', [
        ("aabcc", "dbbca", "aadbbcbcac", True),
        ("aabcc", "dbbca", "aadbbbaccc", False),
        ("", "", "", True),
        ("cabbcaaacacbac", "acabaabacabcca", "cacabaabacaabccbabcaaacacbac", True),
    ])

def test_isInterleave(s1, s2, s3, expected):
    #ans_brute = Solution.isInterleave_brute(s1, s2, s3)
    #assert ans_brute == expected#Took 65.58s to brute force

    #ans_recur_memo = Solution.isInterleave_memo(s1, s2, s3)
    #assert ans_recur_memo == expected

    ans_recur_memo_simple = Solution.isInterleave_memo_simple(s1, s2, s3)
    assert ans_recur_memo_simple == expected