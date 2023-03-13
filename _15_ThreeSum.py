from typing import List

class Solution:
    def threeSum(nums: List[int]) -> List[List[int]]:
        res, numSet = [], set()
        nums.sort()
        for i in range(len(nums)-1):
            l, r = 0, len(nums) - 1
            while l < i and i < r:
                s = nums[i] + nums[l] + nums[r]
                t = [nums[i], nums[l], nums[r]]
                if s == 0:
                    if str(t) not in numSet:
                        res.append(t)
                        numSet.add(str(t))
                    l, r = l + 1, r - 1
                elif s < 0: l += 1
                elif s > 0: r -= 1
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        ans = []
        for i in range(len(nums) - 2):
            #Only keep the first dupicate i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return ans

if __name__ == '__main__':
    print(threeSum([-1,0,1,2,-1,-4]))