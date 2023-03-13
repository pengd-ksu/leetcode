class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return True

class Solution:
    def isToeplitzMatrix_2(self, matrix: List[List[int]]) -> bool:
        groups = {}
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r-c not in groups:
                    groups[r-c] = val
                elif groups[r-c] != val:
                    return False
        return True

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        return all(r == 0 or c == 0 or matrix[r-1][c-1] == val \
            for r, row in enumerate(matrix) \
            for c, val in enumerate(row))