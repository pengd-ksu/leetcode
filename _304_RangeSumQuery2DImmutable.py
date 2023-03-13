class NumMatrix:
    # Time Limit Exceeded. Too many redundent computations
    def __init__(self, matrix: List[List[int]]):
        self.data = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for row in range(row1, row2 + 1):
            for col in range(col1, col2 + 1):
                total += self.data[row][col]
        return total

class NumMatrix:
    # Pre-computation all the way down in the matrix
    def __init__(self, matrix: List[List[int]]):
        self.sum_matrix = matrix
        for row in range(len(matrix) - 2, -1, -1):
            for col in range(len(matrix[0])):
                self.sum_matrix[row][col] = self.sum_matrix[row][col] + self.sum_matrix[row+1][col] 

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        if row2 == len(self.sum_matrix) - 1:#in case out of index range
            for col in range(col1, col2 + 1):
                total += self.sum_matrix[row1][col]
        else:
            for col in range(col1, col2 + 1):
                total += self.sum_matrix[row1][col] - self.sum_matrix[row2+1][col]
        return total

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)