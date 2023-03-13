class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        top = bottom = y
        left = right = x
        for m in range(len(image)):
            for n in range(len(image[0])):
                if image[m][n] == '1':
                    top = min(top, n)
                    bottom = max(bottom, n + 1)
                    left = min(left, m)
                    right = max(right, m + 1)
        return (right - left) * (bottom - top)

class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        def dfs(matrix, x, y):
            nonlocal top, bottom, left, right
            if x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]) or matrix[x][y] == '0':
                return
            if (x, y) not in check:
                check.add((x, y))
                top = min(top, y)
                bottom = max(bottom, y + 1)
                left = min(left, x)
                right = max(right, x + 1)
                dfs(matrix, x + 1, y)
                dfs(matrix, x - 1, y)
                dfs(matrix, x, y + 1)
                dfs(matrix, x, y - 1)
        
        top = bottom = y
        left = right = x
        check = set()
        dfs(image, x, y)
        return (right - left) * (bottom - top)