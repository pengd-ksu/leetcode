class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check_row = defaultdict(set)
        check_col = defaultdict(set)
        box_set = defaultdict(set)
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num != '.':
                    if num in check_row[r] or num in check_col[c] or num in box_set[(r//3,c//3)]:
                        return False
                    else:
                        check_row[r].add(num)
                        check_col[c].add(num)
                        box_set[(r//3,c//3)].add(num)
        return True