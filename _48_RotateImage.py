class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Observation: 90 degree clock rotation is one transpose, plus
        # reverse every element in the row
        def transpose(arr: List[List[int]]) -> None: # In place transpose
            n = len(arr)
            for i in range(n):
                for j in range(i+1, n): # Start from one element after the diagonal
                    arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
                    
        def reverseRow(arr: List[List[int]]) -> None: # Reverse in place
            n = len(arr)
            for i in range(n):
                for j in range(n // 2):
                    arr[i][j], arr[i][n-1-j] = arr[i][n-1-j], arr[i][j]
            
        transpose(matrix)
        reverseRow(matrix)

    def rotate_2(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # [::-1] turn the matrix upside down, then zip will transpose it.
        matrix[:] = zip(*matrix[::-1]) #[:] will keep matrix the same, 
        # while matrix = will assignment a new reference named matrix