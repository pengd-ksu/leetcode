from typing import List
from pytest import mark

class Solution:
    def solve_connection(board: List[List[str]]) -> None:
        if not board:
            return

        m, n = len(board), len(board[0])
        periphery = [ij for k in range(max(m, n)) for ij in ((0, k), (k, 0), (m-1, k), (k, n-1))]
        while periphery:
            i, j = periphery.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'S'
                periphery += (i, j-1), (i, j+1), (i-1, j), (i+1, j)
        board[:] = [['XO'[c == 'S'] for c in row] for row in board]
        #In the last line 'XO' is a string. [c == 'S'] will return [1] if true, else [0], which
        #will play as index for string 'XO'. 'XO'[0] is 'X' and 'XO'[1] is 'O'

    def solve_connection(board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #Start searching for O in the border, stop with ExpandToAll to get all of the 
        #connected Os in a dict. Then check them with ConnectToBorder, if yes, set all
        #of them as X, then continue searching.
        
        #Expand to all O that connects together. Store them in a dict with position as key
        def ExpandToAllConnected(i, j, ConnectedSet):
            #nonlocal m, n
            if board[i][j] == 'O':
                ConnectedSet.add((i, j))
            else:
                return
            if (i + 1 <= m - 1) and ((i + 1, j) not in ConnectedSet):
                ExpandToAllConnected(i + 1, j, ConnectedSet)
            if (i - 1 >= 0) and ((i - 1, j) not in ConnectedSet):
                ExpandToAllConnected(i - 1, j, ConnectedSet)
            if (j + 1 <= n - 1) and ((i, j + 1) not in ConnectedSet):
                ExpandToAllConnected(i, j + 1, ConnectedSet)
            if (j - 1 >= 0) and ((i, j - 1) not in ConnectedSet):
                ExpandToAllConnected(i, j - 1, ConnectedSet)
            return
                
        #Check if any connected O is on border. If yes, set all Os in the dict to X.
        def ConnectToBorder(ConnectedSet):
            for key in ConnectedSet:
                i, j = key
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    return True
            return False
        
        m, n = len(board), len(board[0])
        ConnectedSet_ToBorader = set()
        ConnectedSet_NotToBorader = set()
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    if (i, j) in ConnectedSet_ToBorader:
                        continue
                    elif (i, j) in ConnectedSet_NotToBorader:
                        board[i][j] = 'X'
                    else:
                        tmp = set()
                        ExpandToAllConnected(i, j, tmp)
                        if ConnectToBorder(tmp):
                            ConnectedSet_ToBorader |= tmp
                            continue
                        else:
                            ConnectedSet_NotToBorader |= tmp
                            board[i][j] = 'X'
        return board

@mark.parametrize('board, expected', [
        ([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]], 
            [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]),
        ([["X"]], [["X"]]),
        ([["O","O","O"],["O","O","O"],["O","O","O"]], 
            [["O","O","O"],["O","O","O"],["O","O","O"]]),
        (
[["O","O","O","O","X","X"],["O","O","O","O","O","O"],["O","X","O","X","O","O"],["O","X","O","O","X","O"],["O","X","O","X","O","O"],["O","X","O","O","O","O"]],
[["O","O","O","O","X","X"],["O","O","O","O","O","O"],["O","X","O","X","O","O"],["O","X","O","O","X","O"],["O","X","O","X","O","O"],["O","X","O","O","O","O"]]),
        ([["O","X","O","O","X","X"],["O","X","X","X","O","X"],["X","O","O","X","O","O"],["X","O","X","X","X","X"],["O","O","X","O","X","X"],["X","X","O","O","O","O"]],
            [["O","X","O","O","X","X"],["O","X","X","X","O","X"],["X","O","O","X","O","O"],["X","O","X","X","X","X"],["O","O","X","O","X","X"],["X","X","O","O","O","O"]]),
    ])

def test_solve(board, expected):
    ans = Solution.solve(board)
    assert ans == expected
