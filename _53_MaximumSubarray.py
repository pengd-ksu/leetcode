from typing import List

class Solution:
    def maxSubArray_brute(nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        max_value = float('-inf')
        for i in range(len(nums)):
            for j in range(i + 1):
                n = sum(nums[j:i + 1])
                if n > max_value:
                    max_value = n
                    #print(f'i: {i}, j: {j}')
        return max_value

    def maxSubArray_dp(nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        dp = [float('-inf')] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        return max(dp)

    def maxSubArray_dp2(self, nums: List[int]) -> int:
        # dp[i] is the largest contiguous subarray till index i. It could be
        # either only nums[i], or last largest subarray till nums[i] (included)
        dp = [n for n in nums]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        return max(dp)

if __name__ == '__main__':
    #print(Solution.maxSubArray_brute([-2,1,-3,4,-1,2,1,-5,4]))
    #print(Solution.maxSubArray_brute([5,4,-1,7,8]))
    print(Solution.maxSubArray_dp([-2, 1]))