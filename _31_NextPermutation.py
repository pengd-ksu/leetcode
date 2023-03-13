class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(arr, i, j):
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
        
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i >= 0:
            for j in range(len(nums) - 1, -1, -1):
                if nums[j] > nums[i]:
                    break
            swap(nums, i, j)
        # The sorted() function will return a list so you must assign the returned data to a new variable. The sort() function modifies the list in-place and has no return value.
        nums[i+1:] = sorted(nums[i+1:])
        return nums

class Solution:
    def reverse(self, nums):
        # In place reverse.
        i, j = 0, len(nums) - 1
        while i < j:
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            i += 1
            j -= 1
            
    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
        
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0:
            return self.reverse(nums)
        
        i -= 1
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        
        self.swap(nums, i, j)
        nums[(i+1):] = sorted(nums[(i+1):])
        return nums

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = len(nums) - 1
        while idx > 0:
            if nums[idx - 1] < nums[idx]:#we are looking for such idx-1
                break
            idx -= 1
        if idx == 0:# The nums array is in descending order
            return self.reverse(nums)
        idx -= 1
        for i in range(len(nums) - 1, idx, -1):
            if nums[i] > nums[idx]:
                self.swap(nums, i, idx)
                nums[(idx+1):] = sorted(nums[(idx+1):])# This will be the nex in order.
                break

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = len(nums) -1 
        while idx > 0 and nums[idx-1] >= nums[idx]:
            idx -= 1
        if idx == 0:
            return self.reverse(nums)
        idx -= 1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > nums[idx]:
                self.swap(nums, i, idx)
                break
        nums[idx+1:] = sorted(nums[idx+1:])
        return nums

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(arr, i, j):
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
            
        idx = len(nums) - 1
        while idx > 0 and nums[idx-1] >= nums[idx]:
            idx -= 1
        if idx == 0:
            nums.sort()
            return#sorted(nums)#In-place!
        
        idx -= 1
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] > nums[idx]:
                swap(nums, j, idx)
                break
        nums[idx+1:] = sorted(nums[idx+1:])
        return nums