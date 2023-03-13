class Solution:
    def findDuplicates_1(self, nums: List[int]) -> List[int]:
        nums.sort()#cost nlgn, but it requires to be O(n)
        ans = set()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                ans.add(nums[i + 1])
        return list(ans)

    def findDuplicates_2(self, nums: List[int]) -> List[int]:
        #This is O(n) and takes advantage that the number will at most appear twice
        length = len(nums)
        for n in nums:
            idx = (abs(n) - 1) % length
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
            else:
                nums[idx] = -nums[idx] + length#Second time it will be out of range
        return [idx + 1 for idx, n in enumerate(nums) if n > length]

    def findDuplicates_3(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            abn = abs(n)
            idx = abn - 1
            if nums[idx] < 0:
                ans.append(abn)
            else:
                nums[idx] = -nums[idx]
        return ans