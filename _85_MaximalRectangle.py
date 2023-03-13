class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        #Inspired by leetcode 84
        n = len(matrix[0])
        heights = [0] * (n + 1)
        area = 0
        for row in matrix:
            for i in range(n):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            stack = [-1]
            for i in range(n + 1):
                while heights[i] < heights[stack[-1]]:
                    idx = stack.pop()
                    h = heights[idx]
                    area = max(area, h * (i - stack[-1] - 1))
                stack.append(i)
        return area
