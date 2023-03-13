class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque()
        fresh = 0
        visit = set()
        record = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2 and (i, j) not in visit:
                    visit.add((i, j))
                    queue.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh += 1
        while queue:
            r, c, minute = queue.popleft()
            record = minute
            grid[r][c] = 2
            for r_diff, c_diff in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                r_new, c_new = r + r_diff, c + c_diff
                if 0 <= r_new < len(grid) and 0 <= c_new < len(grid[0]) and grid[r_new][c_new] == 1 and (r_new, c_new) not in visit:
                    visit.add((r_new, c_new))
                    queue.append((r_new, c_new, minute + 1))
                    fresh -= 1
        return record if fresh == 0 else -1

class Solution:# Optimization with visit. Reuse grid in place to keep track of visit
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque()
        fresh = 0
        record = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh += 1
        while queue:
            r, c, minute = queue.popleft()
            record = minute
            grid[r][c] = 2
            for r_diff, c_diff in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                r_new, c_new = r + r_diff, c + c_diff
                if 0 <= r_new < len(grid) and 0 <= c_new < len(grid[0]) and grid[r_new][c_new] == 1:
                    grid[r_new][c_new] = 2
                    queue.append((r_new, c_new, minute + 1))
                    fresh -= 1
        return record if fresh == 0 else -1

from collections import deque # Official approach 1
class Solution:#a delimiter (i.e. (row=-1, col=-1)) in the queue to separate 
    # cells on different levels. 
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()

        # Step 1). build the initial set of rotten oranges
        fresh_oranges = 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        # Mark the round / level, _i.e_ the ticker of timestamp
        queue.append((-1, -1))

        # Step 2). start the rotting process via BFS
        minutes_elapsed = -1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while queue:
            row, col = queue.popleft()
            if row == -1:
                # We finish one round of processing
                minutes_elapsed += 1
                if queue:  # to avoid the endless loop
                    queue.append((-1, -1))
            else:
                # this is a rotten orange
                # then it would contaminate its neighbors
                for d in directions:
                    neighbor_row, neighbor_col = row + d[0], col + d[1]
                    if ROWS > neighbor_row >= 0 and COLS > neighbor_col >= 0:
                        if grid[neighbor_row][neighbor_col] == 1:
                            # this orange would be contaminated
                            grid[neighbor_row][neighbor_col] = 2
                            fresh_oranges -= 1
                            # this orange would then contaminate other oranges
                            queue.append((neighbor_row, neighbor_col))

        # return elapsed minutes if no fresh orange left
        return minutes_elapsed if fresh_oranges == 0 else -1

class Solution(object): # Official approach 2
    def orangesRotting(self, grid):
        ROWS, COLS = len(grid), len(grid[0])

        # run the rotting process, by marking the rotten oranges with the timestamp
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        def runRottingProcess(timestamp):
            # flag to indicate if the rotting process should be continued
            to_be_continued = False
            for row in range(ROWS):
                for col in range(COLS):
                    if grid[row][col] == timestamp:
                        # current contaminated cell
                        for d in directions:
                            n_row, n_col = row + d[0], col + d[1]
                            if ROWS > n_row >= 0 and COLS > n_col >= 0:
                                if grid[n_row][n_col] == 1:
                                    # this fresh orange would be contaminated next
                                    grid[n_row][n_col] = timestamp + 1
                                    to_be_continued = True
            return to_be_continued
 Ba b1  Q        timestamp = 2
        while runRottingProcess(timestamp):
            timestamp += 1
        # end of process, to check if there are still fresh oranges left
        for row in grid:
            for cell in row:
                if cell == 1:  # still got a fresh orange left
                    return -1
        # return elapsed minutes if no fresh orange left
        return timestamp - 2