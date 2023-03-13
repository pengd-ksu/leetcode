class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        maxcut = max(ribbons)
        mincut = 1
        
        while mincut <= maxcut:
            mid = (mincut + maxcut) // 2
            cnt = 0
            for r in ribbons:
                cnt += r // mid
            if cnt >= k:
                mincut = mid + 1
            else:
                maxcut = mid - 1
        
        return maxcut
    #Return the maximum possible positive integer length that you can 
    # obtain k ribbons of. So return the largest possible cut.