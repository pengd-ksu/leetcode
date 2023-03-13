from typing import List
from pytest import mark

class Solution:
    def searchInsert(nums: List[int], target: int) -> int:
        if not nums or target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def searchInsert_2(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

"""
@mark.parametrize('nums, target, expected', [
        ([4,5,6,7,0,1,2], 0, 4),
        ([4,5,6,7,0,1,2], 3, -1),
        ([1], 0, -1),
    ])

def test_search(nums, target, expected):
    ans = Solution.search(nums, target)
    assert ans == expected