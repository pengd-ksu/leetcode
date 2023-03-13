from typing import List

class Solution:
    def findMin_1(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[left] > nums[right]:
                preLeft = left
                left = mid + 1
            else:#nums[left] < nums[right], because nums contain unique numbers
                if left > 0 and nums[left - 1] < nums[left]:
                    left, right = preLeft + 1, left - 1
                else:
                    return nums[left]

    def findMin_2(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else: #nums[mid] < nums[high] because nums contain uniqe numbers
                high = mid

        return nums[low]