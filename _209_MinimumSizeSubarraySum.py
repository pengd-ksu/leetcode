class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        ans = float('inf')
        left = 0
        
        for i in range(len(nums)):
            total += nums[i]
            while total >= target:
                ans = min(ans, i - left + 1)
                total -= nums[left]
                left += 1
            
        return ans if ans != float('inf') else 0

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, res = 0, len(nums) + 1
        for j in range(len(nums)):
            target -= nums[j]
            while target <= 0:
                res = min(res, j - i + 1)
                target += nums[i]
                i += 1
        return res % (len(nums) + 1)
    # When there is none, modular will return 0