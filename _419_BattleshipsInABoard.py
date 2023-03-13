class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X' and not (i > 0 and board[i-1][j] == 'X') and not (j > 0 and board[i][j-1] == 'X'):
                    count += 1
        return count