from typing import List
from pytest import mark

class Solution:
    def search(nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
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
        return -1

    def search_2(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target: return mid
            
            # inflection point to the right. Left is strictly increasing
            if nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
                    
            # inflection point to the left of me. Right is strictly increasing
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

    def search_3(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[right]:# Distinct values
                # Right part is strictly ascending
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target <= nums[right]:
                    left = mid + 1
                elif nums[mid] < target and target > nums[right]:
                    right = mid - 1
                    
            else:# Left part is strictly ascending
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target >= nums[left]:
                    right = mid - 1
                elif nums[mid] > target and nums[left] > target:
                    left = mid + 1
        return -1

@mark.parametrize('nums, target, expected', [
        ([4,5,6,7,0,1,2], 0, 4),
        ([4,5,6,7,0,1,2], 3, -1),
        ([1], 0, -1),
    ])

def test_search(nums, target, expected):
    ans = Solution.search(nums, target)
    assert ans == expected