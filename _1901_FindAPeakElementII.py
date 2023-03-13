class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        def findMax(row: List[int]) -> int:
            maxNum = float('-inf')
            for j in range(len(row)):
                if row[j] > maxNum:
                    maxNum = row[j]
                    index = j
            return index
        m = len(mat) - 1
        lo, hi = 0, m
        while lo < hi:
            mid = (lo + hi) // 2
            cidx = findMax(mat[mid])
            loIsBig = mid > lo and mat[mid][cidx] < mat[mid-1][cidx]
            hiIsBig = mid < hi and mat[mid][cidx] < mat[mid+1][cidx]
            
            if not loIsBig and not hiIsBig:
                return [mid, cidx]
            
            if loIsBig:
                hi = mid - 1
            else:#hiIsBig
                lo = mid + 1
        return [lo, cidx]#or lo <= hi, without this return could also get right result