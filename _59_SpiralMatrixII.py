class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        advance = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = 0
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        x, y = 0, 0
        for entry in range(1, n * n + 1):
            matrix[x][y] = entry
            dx, dy = advance[direction]
            if -1 < x + dx < n and -1 < y + dy < n and matrix[x+dx][y+dy] == 0:
                x = x + dx
                y = y + dy
            else:
                direction = (direction + 1) % 4
                dx, dy = advance[direction]
                x, y = x + dx, y + dy
        return matrix

    def generateMatrix_2(self, n: int) -> List[List[int]]:
        A, lo = [], n*n+1
        while lo > 1:
            lo, hi = lo - len(A), lo
            A = [list(range(lo, hi))] + [*zip(*A[::-1])]
        return A