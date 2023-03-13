class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        set_nums = set()
        n = 0
        for index, i in enumerate(nums):
            if i not in set_nums:
                set_nums.add(i)
                nums[n] = nums[index]
                n += 1
        return n

    def removeDuplicates_2(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        
        duplicate = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[duplicate-1]:
                nums[duplicate] = nums[i]
                duplicate += 1
        return duplicate