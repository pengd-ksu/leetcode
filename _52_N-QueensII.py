class Solution:
    def totalNQueens(self, n: int) -> int:
        path = []
        result = []
        col = set()
        diag = set()
        anti_diag = set()
        def backtrack_queen(r: int) -> List[List[str]]:
            if r == n:
                result.append(list(path))
                return
            for c in range(n):
                if c in col or (r + c) in diag or (c - r) in anti_diag:
                    continue
                col.add(c)
                diag.add(r + c)
                anti_diag.add(c - r)
                path.append(c * '.' + 'Q' + '.' * (n - c - 1))
                
                backtrack_queen(r + 1)
                
                col.remove(c)
                diag.remove(r + c)
                anti_diag.remove(c - r)
                path.pop()
        
        backtrack_queen(0)
        return len(result)