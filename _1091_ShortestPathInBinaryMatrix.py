class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        visited = set()
        visited.add((0, 0))
        queue = collections.deque()
        queue.append((0, 0, 1))
        while queue:
            row, col, step = queue.popleft()
            if row == col == n - 1:
                return step
            for directions in ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)):
                new_row, new_col = row + directions[0], col + directions[1]
                if 0 <= new_row < n and 0 <= new_col < n and grid[new_row][new_col] == 0 and (new_row, new_col) not in visited:
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col, step + 1))
        return -1

class Solution: # Approach 1: Breadth-first Search (BFS), Overwriting Input
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        directions = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        # Helper function to find the neighbors of a given cell.
        def get_neighbours(row, col):
            for row_difference, col_difference in directions:
                new_row = row + row_difference
                new_col = col + col_difference
                if not(0 <= new_row <= max_row and 0 <= new_col <= max_col):
                    continue
                if grid[new_row][new_col] != 0:
                    continue
                yield (new_row, new_col)
        
        # Check that the first and last cells are open.
        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1
        
        # Set up the BFS.
        queue = deque()
        queue.append((0, 0))
        grid[0][0] = 1
        
        # Carry out the BFS.
        while queue:
            row, col = queue.popleft()#Must pop from left. pop() is from right.
            distance = grid[row][col]
            if (row, col) == (max_row, max_col):
                return distance
            for neighbour_row, neighbour_col in get_neighbours(row, col):
                grid[neighbour_row][neighbour_col] = distance + 1
                queue.append((neighbour_row, neighbour_col))
        
        # There was no path.
        return -1

class Solution: # Approach 2: Breadth-first Search (Without Overwriting the Input)
    def shortestPathBinaryMatrix_2(self, grid: List[List[int]]) -> int:
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
        
        def get_neighbours(row, col):
            for row_difference, col_difference in directions:
                new_row = row + row_difference
                new_col = col + col_difference
                if not (0 <= new_row <= max_row and 0 <= new_col <= max_col):
                    continue
                if grid[new_row][new_col] != 0:
                    continue
                yield(new_row, new_col)
                
        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1
        
        import collections
        queue = collections.deque()
        queue.append((0, 0, 1))
        visited = set()
        visited.add((0, 0))
        
        while queue:
            row, col, distance = queue.popleft() # Must pop from left side. pop() is from right side
            if (row, col) == (max_row, max_col):
                return distance
            for neighbour in get_neighbours(row, col):
                if neighbour in visited:
                    continue
                queue.append((*neighbour, distance + 1))
                visited.add(neighbour)
        return -1

class Solution: 
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        directions = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        # Helper function to find the neighbors of a given cell.
        def get_neighbours(row, col):
            for row_difference, col_difference in directions:
                new_row = row + row_difference
                new_col = col + col_difference
                if not(0 <= new_row <= max_row and 0 <= new_col <= max_col):
                    continue
                if grid[new_row][new_col] != 0:
                    continue
                yield (new_row, new_col)
        
        # Check that the first and last cells are open. 
        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1
        
        # Set up the BFS.
        current_layer = [(0, 0)]
        next_layer = []
        visited = {(0, 0)}
        current_distance = 1
        
        while current_layer:
            
            # Process the current layer.
            for row, col in current_layer:
                if (row, col) == (max_row, max_col):
                    return current_distance
                for neighbour in get_neighbours(row, col):
                    if neighbour in visited:
                        continue
                    visited.add(neighbour)
                    next_layer.append(neighbour)
            
            # Set up for processing the next layer.
            current_distance += 1
            current_layer = next_layer
            next_layer = []
                
        # There was no path.
        return -1


class Solution: 
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:  
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        directions = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        # Helper function to find the neighbors of a given cell.
        def get_neighbours(row, col):
            for row_difference, col_difference in directions:
                new_row = row + row_difference
                new_col = col + col_difference
                if not(0 <= new_row <= max_row and 0 <= new_col <= max_col):
                    continue
                if grid[new_row][new_col] != 0:
                    continue
                yield (new_row, new_col)
        
        # Check that the first and last cells are open. 
        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1
        
        # Set up the BFS.
        queue = deque([(0, 0)])
        visited = {(0, 0)}
        current_distance = 1
        
        # Do the BFS.
        while queue:
            # Process all nodes at current_distance from the top-left cell.
            nodes_of_current_distance = len(queue)
            for _ in range(nodes_of_current_distance):
                row, col = queue.popleft()
                if (row, col) == (max_row, max_col):
                    return current_distance
                for neighbour in get_neighbours(row, col):
                    if neighbour in visited:
                        continue
                    visited.add(neighbour)
                    queue.append(neighbour)
            # We'll now be processing all nodes at current_distance + 1
            current_distance += 1
                    
        # There was no path.
        return -1

class Solution: # Approach 3: A* (Advanced)
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        directions = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        # Helper function to find the neighbors of a given cell.
        def get_neighbours(row, col):
            for row_difference, col_difference in directions:
                new_row = row + row_difference
                new_col = col + col_difference
                if not(0 <= new_row <= max_row and 0 <= new_col <= max_col):
                    continue
                if grid[new_row][new_col] != 0:
                    continue
                yield (new_row, new_col)
        
        # Helper function for the A* heuristic.
        # The shorter distance can always be covered by diaganol
        def best_case_estimate(row, col):
            return max(max_row - row, max_col - col)
            
        # Check that the first and last cells are open. 
        if grid[0][0] or grid[max_row][max_col]:
            return -1
        
        # Set up the A* search.
        visited = set()
        # Entries on the priority queue are of the form
        # (total distance estimate, distance so far, (cell row, cell col))
        priority_queue = [(1 + best_case_estimate(0, 0), 1, (0, 0))]
        while priority_queue:
            estimate, distance, cell = heapq.heappop(priority_queue)
            if cell in visited:
                continue
            if cell == (max_row, max_col):
                return distance
            visited.add(cell)
            for neighbour in get_neighbours(*cell):
                # The check here isn't necessary for correctness, but it
                # leads to a substantial performance gain.
                if neighbour in visited:
                    continue
                estimate = best_case_estimate(*neighbour) + distance + 1
                entry = (estimate, distance + 1, neighbour)
                heapq.heappush(priority_queue, entry)
        
        # There was no path.
        return -1