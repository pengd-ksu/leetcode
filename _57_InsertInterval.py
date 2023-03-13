from typing import List

from pytest import mark
import unittest

class Solution:
    def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(interval[1], merged[-1][1])
        return merged

@mark.parametrize('intervals, newInterval, expected',[
    ([[1,3],[6,9]], [2,5], [[1,5],[6,9]]),
    ([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8], [[1,2],[3,10],[12,16]]),
])

def test_spiralOrder(intervals, newInterval, expected):
    ans = Solution.insert(intervals, newInterval)
    assert ans == expected