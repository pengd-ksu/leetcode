from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if (mid == 0 and nums[mid] > nums[mid + 1]) or (mid == len(nums) - 1 and nums[mid] > nums[mid - 1]) or (0 < mid < len(nums) - 1 and nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]):
                return mid
            elif mid > 0 and nums[mid] < nums[mid - 1]:#left priority
                high = mid - 1
            elif mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
                low = mid + 1

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid+1] > nums[mid]:#mid+1 will be at most hi
                lo = mid + 1
            else:
                hi = mid
        return lo

# This variant is for non-strict peak
def findPeakElement_var(nums: List[int]) -> int:
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid+1] >= nums[mid]:#mid+1 will be at most hi
            lo = mid + 1
        else:
            hi = mid
    return lo

nums1 = [1,2,2,0,3,3,2]
nums2 = [1,1,1,1,0]
print(findPeakElement_var(nums2))