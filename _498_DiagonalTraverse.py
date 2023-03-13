class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # For cells in the same diagonal, their sum of indices are the same, 
        # like (0,1) and (1,0). We add the entries by row, and column in a 
        # list with sum of indices as keys. When the indices sum are even, 
        # it goes back from the list.
        ans = []
        diag = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                diag[i+j].append(mat[i][j])
        for j in range(len(mat) + len(mat[0]) + 1):
            if j % 2 == 0:
                ans.extend(diag[j][::-1])
            else:
                ans.extend(diag[j])
        return ans