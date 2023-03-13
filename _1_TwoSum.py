class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i]+nums[j] == target):
                    return [i, j]

    def twoSum_2(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return[d[m], i]
            else:
                d[n] = i

    def twoSum_3(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if target - nums[i] in d.keys():
                return [i, d[target - nums[i]]]
            else:
                d[nums[i]] = i