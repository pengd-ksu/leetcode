from typing import List

from pytest import mark

class Solution(object):
    def setZeroes(matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        #Use the first ele in a row as a flag for the whole row,
        #if one of the ele in the row is 0.
        #Same for first ele in a column.
        #matrix[0][0] is a special location, set a variable
        #isFirstCol for indicating flag for the first column
        is_col = False
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R):
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, C):
                # If an element is zero, we set the first element of the corresponding row and column to 0
                if matrix[i][j]  == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # Iterate over the array once again and using the first row and first column, update the elements.
        for i in range(1, R):
            for j in range(1, C):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        # See if the first row needs to be set to zero as well
        if matrix[0][0] == 0:
            for j in range(C):
                matrix[0][j] = 0

        # See if the first column needs to be set to zero as well        
        if is_col:
            for i in range(R):
                matrix[i][0] = 0

        return matrix

@mark.parametrize('matrix, expected', [
        ([[1,1,1],[1,0,1],[1,1,1]], [[1,0,1],[0,0,0],[1,0,1]]),
        ([[0,1,2,0],[3,4,5,2],[1,3,1,5]], [[0,0,0,0],[0,4,5,0],[0,3,1,0]]),
    ])

def test_setZeroes(matrix, expected):
    ans = Solution.setZeroes(matrix)
    assert ans == expected