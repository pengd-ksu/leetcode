class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0:
            return
        cnums = nums[-k:] + nums[:len(nums)-k]
        for i in range(len(cnums)):
            nums[i] = cnums[i]

    def rotate_2(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(arr, i, j):#reverse arr from index i to j (both inclusive)
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        
        k = k % len(nums)
        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, len(nums) - 1)