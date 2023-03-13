from typing import List
from pytest import mark

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            elif nums[start] == nums[end] == target:
                return [start, end]
            elif nums[start] != target:
                start += 1
            else:
                end -= 1
        return [-1, -1]

    def searchRange_2(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left, right = 0, len(nums) - 1
        while left <= right: # '=' just in case there's only one number in nums
            mid = (left + right) // 2
            if nums[mid] == target:
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if nums[mid] != target:
            return [-1, -1]
        lo, hi = mid, mid
        while lo - 1 >= 0 and nums[lo-1] == target:
            lo -= 1
        while hi + 1 < len(nums) and nums[hi+1] == target:
            hi += 1
        return [lo, hi]