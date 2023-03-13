class TicTacToe:

    def __init__(self, n: int):
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        # Return player if player wins, or 0 if no one wins
        n = self.n
        def checkDiagonal(player):
            for i in range(n):
                if self.board[i][i] != player:
                    return False
            return True

        def checkAntiDiagonal(player):
            for r in range(n):
                if self.board[r][n-r-1] != player:
                    return False
            return True

        def checkColumn(col, player):
            for r in range(n):
                if self.board[r][col] != player:
                    return False
            return True

        def checkRow(row, player):
            for c in range(n):
                if self.board[row][c] != player:
                    return False
            return True
        self.board[row][col] = player
        if checkRow(row, player) or checkColumn(col, player) or (row == col and checkDiagonal(player)) or (col == n - row - 1 and (checkAntiDiagonal(player))):
            return player
        else:
            return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

class TicTacToe:
    def __init__(self, n: int):
        self.n = n
        self.horizontal = [0] * n#Store sum of col
        self.vertical = [0] * n#Store sum of row
        self.diag1 = 0
        self.diag2 = 0

    def move(self, row: int, col: int, player: int) -> int:
        # Key point: A move is guaranteed to be valid and is placed on an empty block. Therefore, we don't need to worry if any of the move is invalid
        n = self.n
        move = 1 if player == 1 else -1
        if row == col:
            self.diag1 += move
        if row + col == n - 1:
            self.diag2 += move
        self.horizontal[col] += move
        self.vertical[row] += move
        if abs(self.horizontal[col]) == n or abs(self.vertical[row]) == n or abs(self.diag1) == n or abs(self.diag2) == n:
            return player
        else:
            return 0

class TicTacToe:
    def __init__(self, n: int):
        self.count = collections.Counter()
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        n = self.n
        for i, x in enumerate((row, col, row + col, row - col)):
            self.count[i, x, player] += 1
            if self.count[i, x, player] == n:
                return player
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

class TicTacToe(object):
    def __init__(self, n):
        count = collections.Counter()
        def move(row, col, player):
            for i, x in enumerate((row, col, row+col, row-col)):
                count[i, x, player] += 1
                if count[i, x, player] == n:
                    return player
            return 0
        self.move = move