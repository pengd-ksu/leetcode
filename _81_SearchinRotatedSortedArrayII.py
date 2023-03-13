from typing import List
from pytest import mark

class Solution:
    def search(nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            while left < right and nums[left] == nums[left + 1]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[mid] <= nums[right]:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target < nums[mid] and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
        return False

@mark.parametrize('nums, target, expected', [
        ([2,5,6,0,0,1,2], 0, True),
        ([2,5,6,0,0,1,2], 3, False),
    ])

def test_search(nums, target, expected):
    ans = Solution.search(nums, target)
    assert ans == expected