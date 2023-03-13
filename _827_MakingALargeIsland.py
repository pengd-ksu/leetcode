class Solution(object): # naive DFS
    def largestIsland(self, grid):
        # Time Limit Exceeded
        N = len(grid)

        def check(r, c):
            seen = {(r, c)}
            stack = [(r, c)]
            while stack:
                r, c = stack.pop()
                for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                    if (nr, nc) not in seen and 0 <= nr < N and 0 <= nc < N and grid[nr][nc]:
                        stack.append((nr, nc))
                        seen.add((nr, nc))
            return len(seen)

        ans = 0
        has_zero = False
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 0:
                    has_zero = True
                    grid[r][c] = 1
                    ans = max(ans, check(r, c))
                    grid[r][c] = 0

        return ans if has_zero else N*N

class Solution(object): # naive DFS 2
    def largestIsland(self, grid: List[List[int]]) -> int:
        # Time Limit Exceeded
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def get_neighbour(row, col):
            for row_difference, col_difference in directions:
                new_row = row + row_difference
                new_col = col + col_difference
                if not (0 <= new_row <= max_row and 0 <= new_col <= max_col):
                    continue
                if grid[new_row][new_col] == 0:
                    continue
                yield (new_row, new_col)
        
        def check(row, col):
            seen = set()
            seen.add((row, col))
            stack = [(row, col)]
            while stack:
                row, col = stack.pop()
                for cell in get_neighbour(row, col):
                    if cell not in seen:
                        stack.append(cell)
                        seen.add(cell)
            return len(seen)
        
        area = 0
        haszero = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    haszero = True
                    grid[i][j] = 1
                    area = max(area, check(i, j))
                    grid[i][j] = 0
        return area if haszero else len(grid) ** 2

class Solution(object):
    def largestIsland(self, grid):
        N = len(grid)

        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= nr < N and 0 <= nc < N:
                    yield nr, nc

        def dfs(r, c, index):
            ans = 1
            grid[r][c] = index
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:
                    ans += dfs(nr, nc, index)
            return ans

        area = {}
        index = 2
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    area[index] = dfs(r, c, index)
                    index += 1

        ans = max(area.values() or [0])
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0:
                    seen = {grid[nr][nc] for nr, nc in neighbors(r, c) if grid[nr][nc] > 1}
                    ans = max(ans, 1 + sum(area[i] for i in seen))
        return ans