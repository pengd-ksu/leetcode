class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for n in nums:
            idx = abs(n)
            if nums[idx] < 0:
                ans = idx
                break
            nums[idx] = -nums[idx]
        for i in range(len(nums)):
            nums[i] = abs(nums[i])
        return ans