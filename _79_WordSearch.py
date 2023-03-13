from typing import List

from pytest import mark

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(i, j, idx, visited):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[idx] or (i, j) in visited:
                return False
            elif idx == len(word) - 1:
                return True
            else:
                visited.add((i, j))
                result = dfs(i+1, j, idx+1, visited) or dfs(i-1, j, idx+1, visited) or dfs(i, j+1, idx+1, visited) or dfs(i, j-1, idx+1, visited)
                visited.remove((i, j)) # Must be removed because the other routes could be different than the current one. It's only to prune in the current route
            return result
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0, set()):
                        return True
        return False

class Solution:
    def exist(self, board, word):
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.backtrack(row, col, word):
                    return True

        # no match found after all exploration
        return False

    def backtrack(self, row, col, suffix):
        """
            backtracking with side-effect,
               the matched letter in the board would be marked with "#".
        """
        # bottom case: we find match for each letter in the word
        if len(suffix) == 0:
            return True
        # Check the current status, before jumping into backtracking
        if row < 0 or row == self.ROWS or col < 0 or col == self.COLS \
                or self.board[row][col] != suffix[0]:
            return False
        # mark the choice before exploring further.
        self.board[row][col] = '#'
        # explore the 4 neighbor directions
        for rowOffset, colOffset in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
            # sudden-death return, no cleanup.
            if self.backtrack(row + rowOffset, col + colOffset, suffix[1:]):
                return True
        # revert the marking
        self.board[row][col] = suffix[0]
        # Tried all directions, and did not find any match
        return False

class Solution:
    def exist(self, board, word):
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.backtrack(row, col, word):
                    return True

        # no match found after all exploration
        return False

    def backtrack(self, row, col, suffix):
        # bottom case: we find match for each letter in the word
        if len(suffix) == 0:
            return True
        # Check the current status, before jumping into backtracking
        if row < 0 or row == self.ROWS or col < 0 or col == self.COLS \
                or self.board[row][col] != suffix[0]:
            return False
        ret = False
        # mark the choice before exploring further.
        self.board[row][col] = '#'
        # explore the 4 neighbor directions
        for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ret = self.backtrack(row + rowOffset, col + colOffset, suffix[1:])
            # break instead of return directly to do some cleanup afterwards
            if ret: break
        # revert the change, a clean slate and no side-effect
        self.board[row][col] = suffix[0]
        # Tried all directions, and did not find any match
        return ret

class Solution:
    def exist(board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board) - 1, len(board[0]) - 1
        
        def dfs(row: int, col: int, idx: int) -> bool:
            if row > ROW or col > COL or row < 0 or col < 0 or board[row][col] != word[idx]:
                return False
            if idx == len(word) - 1:
                return True
            tmp = board[row][col]
            board[row][col] = '!'#so that it will not be used in the test again
            result = dfs(row+1, col, idx+1) or dfs(row-1, col, idx+1) or dfs(row, col+1, idx+1) or dfs(row, col-1, idx+1)
            board[row][col] = tmp#set back to the original value, because in main it will move
            #to the next cell
            return result
        
        for r in range(ROW+1):
            for c in range(COL+1):
                if dfs(r, c, 0):#Shouldn't return dfs here, because some dfs might return False
                    #in the first if predicate.
                    return True
        return False

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board) - 1, len(board[0]) - 1
        
        def dfs(row: int, col: int, idx: int):
            # row and col are the location of the letter, idx is the index of the letter currently searched for in the word.
            if idx == len(word):
                return True            
            if row > ROW or row < 0 or col > COL or col < 0 or board[row][col] != word[idx]:
                return False
            tmp = board[row][col]
            board[row][col] = '#'# So that it won't touch back again, otherwise it will return False
            result = dfs(row+1, col, idx+1) or dfs(row-1, col, idx+1) or dfs(row, col+1, idx+1) or dfs(row, col-1, idx+1)
            board[row][col] = tmp
            return result
        
        for m in range(ROW+1):
            for n in range(COL+1):
                if dfs(m, n, 0):
                    return True
        return False

@mark.parametrize('board, word, expected', [
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED", True),
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE", True),
    ])

def test_exist(board, word, expected):
    ans = Solution.exist(board, word)
    assert ans == expected


[["A","B","C","E"],
 ["S","F","E","S"],
 ["A","D","E","E"]]
"ABCESEEEFS"