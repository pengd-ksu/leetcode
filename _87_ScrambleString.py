import functools
from typing import List
from pytest import mark

class Solution:
    def isScramble(s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        @functools.cache
        def solve(s1,s2):
            n = len(s1)
            if s1 == s2:
                return True
            if n <= 1:
                return False
            flag = False
            for i in range(1,n):
                cond1 = solve(s1[:i],s2[:i]) and solve(s1[i:],s2[i:])
                cond2 = solve(s1[:i],s2[-i:]) and solve(s1[i:],s2[:-i])
                if cond1 or cond2:
                    flag=True
                    break
            return flag
        return solve(s1,s2)

@mark.parametrize('s1, s2, expected', [
        ("great", "rgeat", True),
        ("abcde", "caebd", False),
        ("a", "a", True),
        ("eebaacbcbcadaaedceaaacadccd", "eadcaacabaddaceacbceaabeccd", False)
    ])

def test_isScramble(s1, s2, expected):
    ans = Solution.isScramble(s1, s2)
    assert ans == expected