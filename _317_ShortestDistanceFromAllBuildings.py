class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.grid = []
        self.distance = []
        
    def bfs(self, r, c):
        if self.grid[r][c] != 1:
            return
        marked = [[False] * self.n for _ in range(self.m)]
        queue = deque()
        queue.append((r, c, 0))
        while queue:
            r, c, n = queue.popleft()
            
            if self.distance[r][c] != None:
                self.distance[r][c] += n
            
            # up
            if r > 0 and self.grid[r-1][c] == 0 and (not marked[r-1][c]):
                queue.append((r - 1, c, n + 1))
                marked[r-1][c] = True
            # down
            if r < (self.m - 1) and self.grid[r+1][c] == 0 and (not marked[r+1][c]):
                queue.append((r + 1, c, n + 1))
                marked[r+1][c] = True
            # left
            if c > 0 and self.grid[r][c-1] == 0 and (not marked[r][c-1]):
                queue.append((r, c - 1, n + 1))
                marked[r][c-1] = True
            # right
            if c < (self.n - 1) and self.grid[r][c+1] == 0 and (not marked[r][c+1]):
                queue.append((r, c + 1, n + 1))
                marked[r][c+1] = True
            
        # find empty lands not reachable from current home and mark them as None (Not valid)
        for r in range(self.m):
            for c in range(self.n):
                if not marked[r][c] and self.grid[r][c] == 0:
                    self.distance[r][c] = None

    def shortestDistance(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.m = len(self.grid)
        if self.m == 0:
            return -1
        self.n = len(self.grid[0])
        if self.n == 0:
            return -1
        self.distance = [[0] * self.n for _ in range(self.m)]
        for r in range(self.m):
            for c in range(self.n):
                if self.grid[r][c] == 1:
                    self.bfs(r, c)

        minDistance = None
        for r in range(self.m):
            for c in range(self.n):
                if self.distance[r][c] and self.grid[r][c] == 0:
                    if minDistance:
                        minDistance = min(minDistance, self.distance[r][c])
                    else:
                        minDistance = self.distance[r][c]
        
        return minDistance if minDistance else -1


class Solution:
    # Approach 2
    def shortestDistance(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        total_sum = [[0] * cols for _ in range(rows)]
        
        def bfs(row, col, curr_count):
            min_distance = math.inf
            queue = deque()
            queue.append([row, col, 0])
            while queue:
                curr_row, curr_col, curr_step = queue.popleft()
                for d in dirs:
                    next_row = curr_row + d[0]
                    next_col = curr_col + d[1]
                    if 0 <= next_row < rows and 0 <= next_col < cols and \
                    grid[next_row][next_col] == -curr_count:
                        total_sum[next_row][next_col] += curr_step + 1
                        min_distance = min(min_distance, total_sum[next_row][next_col])
                        grid[next_row][next_col] -= 1
                        queue.append([next_row, next_col, curr_step + 1])
            return min_distance

        count = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    min_distance = bfs(row, col, count)
                    count += 1
                    if min_distance == math.inf:
                        return -1
        
        return min_distance

class Solution:
    def shortestDistance(self, grid):
        """
        Use hit to record how many times a 0 grid has been reached and use 
        distSum to record the sum of distance from all 1 grids to this 0 grid. 
        A powerful pruning is that during the BFS we use count1 to count how 
        many 1 grids we reached. If count1 < buildings then we know not all 
        1 grids are connected are we can return -1 immediately, which greatly 
        improved speed (beat 100% submissions).
        """
        if not grid or not grid[0]:
            return -1
        M, N = len(grid), len(grid[0])
        buildings = sum(val for line in grid for val in line if val == 1)
        hit = [[0] * N for _ in range(M)]
        distSum = [[0] * N for _ in range(M)]
        
        def BFS(start_x, start_y):
            visited = [[False] * N for _ in range(M)]
            visited[start_x][start_y] = True, 
            count1 = 1
            queue = collections.deque([(start_x, start_y, 0)])
            while queue:
                x, y, dist = queue.popleft()
                for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if 0 <= i < M and 0 <= j < N and not visited[i][j]:
                        visited[i][j] = True
                        if not grid[i][j]:
                            queue.append((i, j, dist + 1))
                            hit[i][j] += 1
                            distSum[i][j] += dist + 1
                        elif grid[i][j] == 1:
                            count1 += 1
            return count1 == buildings

        for x in range(M):
            for y in range(N):
                if grid[x][y] == 1:
                    if not BFS(x, y):
                        return -1
        return min([distSum[i][j] for i in range(M) for j in range(N) if not grid[i][j] and hit[i][j] == buildings] or [-1])