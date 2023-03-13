class Solution: # Time: O(n), Space: O(n)
    def getMaxLen(self, nums: List[int]) -> int:
        pos = [0] * len(nums)
        neg = [0] * len(nums)
        if nums[0] > 0:
            pos[0] = 1
        elif nums[0] < 0:
            neg[0] = 1
        
        ans = pos[0]
        for i in range(1, len(nums)):
            if nums[i] > 0:
                pos[i] = 1 + pos[i-1]
                neg[i] = 1 + neg[i-1] if neg[i-1] > 0 else 0
            elif nums[i] < 0:
                neg[i] = 1 + pos[i-1]
                pos[i] = 1 + neg[i-1] if neg[i-1] > 0 else 0
            ans = max(ans, pos[i])
            
        return ans

class Solution: # Time: O(n), Space: O(1). Only keep the previous pos, neg
    def getMaxLen(self, nums: List[int]) -> int:
        pos, neg = 0, 0
        if nums[0] > 0:
            pos = 1
        elif nums[0] < 0:
            neg = 1
        
        ans = pos
        for i in range(1, len(nums)):
            if nums[i] > 0:
                pos = 1 + pos
                neg = 1 + neg if neg > 0 else 0
            elif nums[i] < 0:
                pos, neg = 1 + neg if neg > 0 else 0, 1 + pos
                # Assignment at the same time, otherwise results would be different because they're relying on each other
            else:
                pos = 0
                neg = 0
            ans = max(ans, pos)
            
        return ans