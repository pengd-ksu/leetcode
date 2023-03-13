from typing import List

class Solution:
    def firstMissingPositive_1(self, nums: List[int]) -> int:
        # Good. Running time is n with only constant storage.
        # Rearrange the nums array. Swap the element that points positions
        # within the range of the array. 
        for i in range(len(nums)):
            if 0 < nums[i] <= len(nums):
                # Important to have nums[i] != nums[nums[i] - 1] in while,
                # in case there will be infinite loop during swap.
                while 0 < nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
                    idx = nums[i] - 1# The index that nums[i] points to.
                    nums[i], nums[idx] = nums[idx], nums[i]
        print(nums)
        for i in range(1, len(nums) + 1):
            if i != nums[i-1]:
                return i
        return len(nums) + 1

    def firstMissingPositive_2(self, nums: List[int]) -> int:
        # We are looking range [1, n] inclusive from both ends
        # Exclude all numbers that are either non-positive, or larger than n
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1
        for i in range(n):
            if abs(nums[i]) != n + 1:
                # Set the number that nums[i] (already in range [1, n]) points
                # to (abs(nums[i]) - 1) as negative.
                nums[abs(nums[i]) - 1] = -abs(nums[abs(nums[i]) - 1])
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1

    def firstMissingPositive_sort(nums: List[int]) -> int:#nlogn
        # Not qualified since running time is nlogn
        nums.sort()
        start = 1
        for n in nums:
            if start == n:
                start += 1
        return start

    def firstMissingPositive_set(nums: List[int]) -> int:#n + n storage
        # Not qualified since using n storage
        numSet = set(nums)
        start = 1
        while start in numSet:
            start += 1
        return start

if __name__ == '__main__':
    print(Solution.firstMissingPositive_set(nums=[1,2,0]))
    print(Solution.firstMissingPositive_set(nums=[3,4,-1,1]))
    print(Solution.firstMissingPositive_set(nums=[7,8,9,11,12]))