class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        def nextStep(cell):
        #check the bound, like 1 and 6. Both need to be kept.
            cell = cell - 1
            row = cell // n
            if row % 2 == 0:
                row = n - row - 1
                col = cell % n
            else:
                row = n - row - 1
                col = n - 1 - cell % n
            return row, col
        
        seen = set()
        queue = collections.deque()
        cell = 1
        step = 0
        queue.append((cell, step))
        while queue:
            cell, step = queue.popleft()
            row, col = nextStep(cell)
            if board[row][col] != -1:
                cell = board[row][col]
            if cell == n * n:
                return step
            for i in range(1, 7):# At most 6
                next_cell = cell + i
                if next_cell <= n * n and next_cell not in seen:
                    seen.add(next_cell)
                    queue.append((next_cell, step + 1))
        return -1

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        need = {1: 0}
        bfs = [1]
        for x in bfs:
            for i in range(x + 1, x + 7):
                a, b = (i - 1) // n, (i - 1) % n
                nxt = board[~a][b if a % 2 == 0 else ~b]
                if nxt > 0: i = nxt
                if i == n * n: return need[x] + 1
                if i not in need:
                    need[i] = need[x] + 1
                    bfs.append(i)
        return -1