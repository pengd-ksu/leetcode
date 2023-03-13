class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        numDict = {}
        for i in range(1, len(nums) + 1):
            numDict[i] = False
        for n in nums:
            numDict[n] = True
        for num in numDict:
            if numDict[num] == False:
                ans.append(num)
        return ans

    def findDisappearedNumbers_2(self, nums: List[int]) -> List[int]:
        for n in nums:
            idx = abs(n) - 1
            nums[idx] = -abs(nums[idx])
        return [i+1 for i, num in enumerate(nums) if num > 0]