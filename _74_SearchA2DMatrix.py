class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == len(matrix[0]) == 1:
            return matrix[0][0] == target
        loRow, hiRow = 0, len(matrix) - 1
        while loRow < hiRow:
            midRow = (loRow + hiRow) // 2
            if matrix[midRow][0] == target:
                return True
            elif matrix[midRow][0] < target:
                if matrix[midRow][-1] < target:
                    loRow = midRow + 1
                elif matrix[midRow][-1] > target:
                    loRow = midRow
                    break
                else:
                    return True
            else:#matrix[midRow][0] > target
                hiRow = midRow - 1
        left, right = 0, len(matrix[0]) - 1
        while left < right:
            mid = (left + right) // 2
            if matrix[loRow][mid] == target:
                return True
            elif matrix[loRow][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if matrix[loRow][left] == target:
            return True
        return False

    def searchMatrix_2(self, matrix: List[List[int]], target: int) -> bool:
        lo, hi = 0, len(matrix) - 1
        start, end = 0, len(matrix[0]) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if matrix[mid][start] > target >= matrix[lo][start]:
                hi = mid - 1
            elif matrix[mid][end] < target <= matrix[hi][end]:
                lo = mid + 1
            elif matrix[mid][start] <= target <= matrix[mid][end]:
                break
            else:
                return False
        while start <= end:
            half = (start + end) // 2
            if matrix[mid][half] == target:
                return True
            elif matrix[mid][half] > target:
                end = half - 1
            else:
                start = half + 1
        return False

    def searchMatrix_3(self, matrix: List[List[int]], target: int) -> bool:
        # The matrix is a sorted list separate by rows and columns
        m, n = len(matrix), len(matrix[0])
        start, end = 0, m * n - 1
        while start <= end:
            mid = (start + end) // 2
            midRow = mid // n # Get the row
            midCol = mid % n # Get the column
            if matrix[midRow][midCol] == target:
                return True
            elif matrix[midRow][midCol] < target:
                start = mid + 1
            elif matrix[midRow][midCol] > target:
                end = mid - 1
        return False