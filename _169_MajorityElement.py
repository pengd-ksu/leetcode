class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

    def majorityElement_brute(self, nums):
        majority_count = len(nums)//2
        for num in nums:
            count = sum(1 for elem in nums if elem == num)
            if count > majority_count:
                return num

    def majorityElement_2(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]