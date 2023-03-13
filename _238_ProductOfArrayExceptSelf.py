class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Key points: first loop get products of everything on 
        # the left side of index i, second loop get products of 
        # everything on the right side of index i.
        p = 1
        result = []
        for i in range(len(nums)):
            result.append(p)
            p = p * nums[i]
        q = 1
        for j in range(len(nums) - 1, -1, -1):
            result[j] = result[j] * q
            q = q * nums[j]
        return result