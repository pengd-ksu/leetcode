from typing import List

from pytest import mark
import unittest

class Solution:
    def spiralOrder(matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 1:
            return matrix[0]
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        ans = []
        # Four directions in total, 0 for right, 1 for bottom, 2 for left,
        # and 3 for up
        direction = 0
        
        while top <= bottom and left <= right:
            if direction == 0:
                for i in range(left, right + 1):
                    ans.append(matrix[top][i])
                top += 1
            elif direction == 1:
                for i in range(top, bottom + 1):
                    ans.append(matrix[i][right])
                right -= 1
            elif direction == 2:
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1
            else:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1
            direction = (direction + 1) % 4
        return ans


@mark.parametrize('query, expected',[
    ([[1,2,3,4],[5,6,7,8],[9,10,11,12]], [1,2,3,4,8,12,11,10,9,5,6,7]),
    ([[1,2,3],[4,5,6],[7,8,9]], [1,2,3,6,9,8,7,4,5]),
])

def test_spiralOrder(query, expected):
    ans = Solution.spiralOrder(query)
    assert ans == expected