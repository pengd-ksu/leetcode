from typing import List

from pytest import mark
import unittest

class Solution:
    def mySqrt(x: int) -> int:
        if x == 0:
            return x
        lo, hi = 1, x
        while lo <= hi:
            mid = (lo + hi) // 2
            if mid * mid <= x and (mid + 1) * (mid + 1) > x:
                return mid
            elif mid * mid < x:
                lo = mid + 1
            elif mid * mid > x:
                hi = mid - 1

@mark.parametrize('x, expected',[
    (4, 2),
    (8, 2),
    (0, 0)
])

def test_mySqrt(x, expected):
    ans = Solution.mySqrt(x)
    assert ans == expected