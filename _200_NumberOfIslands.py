class Solution:
    def numIslands(self, grid: List[List[str]]) -> int: # Modified cells
        def dfs(grid: List[List[str]], i: int, j: int) -> None:
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
                return
            grid[i][j] = '0'#Mark it as sea, and does a depth first search for its 
            #horizontal and vertical neighbours.
            dfs(grid, i+1, j)
            dfs(grid, i-1, j)
            dfs(grid, i, j+1)
            dfs(grid, i, j-1)
            
        if not grid:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1
        return count

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        cnt = 0
        
        def dfs(r, c):
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == '1' and (r, c) not in visited:
                visited.add((r, c))
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1' and (row, col) not in visited:
                    cnt += 1
                    dfs(row, col)
        
        return cnt

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = sum(grid[i][j] == '1' for i in range(len(grid)) for j in range(len(grid[0])))
        parent = [i for i in range(len(grid) * len(grid[0]))]
        
        def find(x):
            if parent[x] != x:
                return find(parent[x])
            else:
                return parent[x]
        
        def union(x, y):
            nonlocal count
            xroot, yroot = find(x), find(y)
            if xroot == yroot:
                return
            else:
                parent[yroot] = xroot
                count -= 1
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    index = i * len(grid[0]) + j
                    if i < len(grid) - 1 and grid[i+1][j] == '1':
                        union(index, index + len(grid[0]))
                    if j < len(grid[0]) - 1 and grid[i][j+1] == '1':
                        union(index, index + 1)
        return count

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    visited.add((i, j)) # add into visited immediately!
                    q = collections.deque()
                    q.append((i, j))
                    while q:
                        r, c = q.popleft()
                        for dr, dc in (0, 1), (0, -1), (1, 0), (-1, 0):
                            new_r, new_c = r + dr, c + dc
                            if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and grid[new_r][new_c] == '1' and (new_r, new_c) not in visited:
                                visited.add((new_r, new_c))# add into visited immediately!
                                q.append((new_r, new_c))
                    count += 1
        return count