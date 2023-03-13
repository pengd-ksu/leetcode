from typing import List
from pytest import mark

class Solution:
    def minimumTotal_brute(self, triangle: List[List[int]]) -> int:
        #Not sure if this is right, because it didn't pass all the tests due
        #to Time Limit Exceeded
        ans = []
        def recursive(level, index, result):
            if level == len(triangle):
                ans.append(result)
                return
            recursive(level + 1, index, result + triangle[level][index])
            if index < len(triangle[level]) - 1:
                recursive(level + 1, index + 1, result + triangle[level][index + 1])
        recursive(0, 0, 0)
        print(ans)
        return min(ans)

    def minimumTotal_dp_bottomUp(self, triangle: List[List[int]]) -> int:
        h = len(triangle) - 1
        while h != 0:
            for i in range(h):
                triangle[h - 1][i] += min(triangle[h][i], triangle[h][i + 1])
            h -= 1
        print(triangle)
        return triangle[0][0]