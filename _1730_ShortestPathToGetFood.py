# Line breaker in python: \
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        visit = set()
        def bfs(row, col):
            queue = collections.deque()
            queue.append((row, col, 0))#starting point as step 0
            visit.add((row, col))
            while queue:
                r, c, step = queue.popleft()
                if grid[r][c] == '#':
                    return step
                for directions in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                    new_r, new_c = r + directions[0], c + directions[1]
                    if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and \
                    grid[new_r][new_c] != 'X' and (new_r, new_c) not in visit:
                    # Check if next step is doable. Can enter food or empty
                    # Made a mistake as only enter 'O' in the first place
                        visit.add((new_r, new_c))
                        queue.append((new_r, new_c, step + 1))
            return -1
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '*':
                    steps = bfs(r, c)
        return steps