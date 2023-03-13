from typing import List

def solveNQueens(n: int) -> List[List[str]]:
    #no need for row set, because it moves incrementally in rows
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
            
            #move back to try next column
            col.remove(c)
            diag.remove(r + c)
            anti_diag.remove(c - r)
            path.pop()
    
    backtrack_queen(0)
    return result

if __name__ == '__main__':
    print(solveNQueens(4))