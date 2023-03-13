class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        s = sum(nums)
        for i, x in enumerate(nums):
            if leftSum == s - leftSum -x:
                return i
            leftSum += x
        return -1