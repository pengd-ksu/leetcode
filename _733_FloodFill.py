class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        check = image[sr][sc]
        if check == newColor:# It's possible they're the same, then will be endless loop
            return image
        
        def dfs(row, col):
            image[row][col] = newColor
            for row_dif, col_dif in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                new_row, new_col = row + row_dif, col + col_dif
                if 0 <= new_row < len(image) and 0 <= new_col < len(image[0]) and image[new_row][new_col] == check:
                    dfs(new_row, new_col)
        
        dfs(sr, sc)
        return image

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        visited = set()
        max_row, max_col, color = len(image), len(image[0]), image[sr][sc]
        q = collections.deque()
        q.append((sr, sc))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            row, col = q.popleft()
            if 0 <= row < max_row and 0 <= col < max_col and image[row][col] == color and (row, col) not in visited:
                visited.add((row, col))# Don't visit back
                image[row][col] = newColor
                neighbors = [(row + direc[0], col + direc[1]) for direc in directions]
                q.extend(neighbors)
        return image