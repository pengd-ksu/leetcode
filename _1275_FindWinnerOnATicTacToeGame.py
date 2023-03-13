class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # Initialize the board, n = 3 in this problem.
        n = 3
        board = [[0] * n for _ in range(n)]
        
        # Check if any of 4 winning conditions to see if the current player has won.
        def checkRow(row, player_id):
            for col in range(n):
                if board[row][col] != player_id:
                    return False
            return True
        
        def checkCol(col, player_id):
            for row in range(n):
                if board[row][col] != player_id:
                    return False
            return True
        
        def checkDiagonal(player_id):
            for row in range(n):
                if board[row][row] != player_id:
                    return False
            return True
        
        def checkAntiDiagonal(player_id):
            for row in range(n):
                if board[row][n - 1 - row] != player_id:
                    return False
            return True
        
        # Start with player_1.
        player = 1

        for move in moves:
            row, col = move
            board[row][col] = player
            
            # If any of the winning conditions is met, return the current player's id.
            if checkRow(row, player) or checkCol(col, player) or \
            (row == col and checkDiagonal(player)) or \
            (row + col == n - 1 and checkAntiDiagonal(player)):
                return 'A' if player == 1 else 'B'
            
            # If no one wins so far, change to the other player alternatively. 
            # That is from 1 to -1, from -1 to 1.
            player *= -1
            
        # If all moves are completed and there is still no result, we shall check if
        # the grid is full or not. If so, the game ends with draw, otherwise pending.    
        return "Draw" if len(moves) == n * n else "Pending"

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # n stands for the size of the board, n = 3 for the current game.
        n = 3

        # use rows and cols to record the value on each row and each column.
        # diag1 and diag2 to record value on diagonal or anti-diagonal.
        rows, cols = [0] * n, [0] * n
        diag = anti_diag = 0
        
        # Two players having value of 1 and -1, player_1 with value = 1 places first.
        player = 1
        
        for row, col in moves:
            
            # Update the row value and column value.
            rows[row] += player
            cols[col] += player
            
            # If this move is placed on diagonal or anti-diagonal, 
            # we shall update the relative value as well.
            if row == col:            
                diag += player
            if row + col == n - 1:
                anti_diag += player
                
            # check if this move meets any of the winning conditions.
            if any(abs(line) == n for line in (rows[row], cols[col], diag, anti_diag)):
                return "A" if player == 1 else "B"
        
            # If no one wins so far, change to the other player alternatively. 
            # That is from 1 to -1, from -1 to 1.
            player *= -1
            
        # If all moves are completed and there is still no result, we shall check if 
        # the grid is full or not. If so, the game ends with draw, otherwise pending.
        return "Draw" if len(moves) == n * n else "Pending"