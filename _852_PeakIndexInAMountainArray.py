from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if mid + 1 <= len(arr) - 1 and arr[mid] < arr[mid+1]:
                left = mid + 1
            elif mid - 1 >= 0 and arr[mid] < arr[mid-1]:
                right = mid - 1
            elif ((mid + 1 <= len(arr) - 1 and arr[mid] >= arr[mid+1]) and (mid - 1 >= 0 and arr[mid] >= arr[mid-1])) or (mid == 0 and arr[mid] >= arr[mid + 1]) or (mid == len(arr) - 1 and arr[mid] >= arr[mid-1]):
                return mid
        return left

    def peakIndexInMountainArray_linear(self, arr: List[int]) -> int:
        for i in range(len(arr)):#guaranteed to have a peak, so no need for boundary
            if arr[i] > arr[i+1]:
                return i

    def peakIndexInMountainArray_2(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid+1]:
                left = mid + 1
            else:
                right = mid
        return left