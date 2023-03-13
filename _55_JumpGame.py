from typing import List

from pytest import mark
import unittest

class Solution:

    def canJump_brute(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        dp = [False] * len(nums)#float('-inf') for negative infinity
        dp[0] = True
        for i in range(len(nums)):
            for j in range(i, min(i + nums[i] + 1, len(nums))):
                if dp[i] == True:
                    dp[j] = True
        return dp[-1] == True

    def canJump_brtue2(self, nums: List[int]) -> bool:
        # Time Limit Exceeded, because there're lots of redundancies.
        dp = [False] * len(nums)
        dp[0] = True
        for i in range(len(nums)):
            steps = nums[i]
            for s in range(steps + 1):
                if i + s < len(dp):
                    dp[i+s] = True if dp[i]==True else False
        return dp[-1] == True

    def canJump_greedy(self, nums: List[int]) -> bool:
        n = len(nums)
        lastpos = n - 1
        for i in range(n - 2, -1, -1):
            if i + nums[i] >= lastpos:
                lastpos = i
        return lastpos == 0

    def canJump_dp(self, nums: List[int]) -> bool:
        # Backward dp, similar to canJump_brtue2 with more pruning.
        N = len(nums)
        dp = [False]*(N)
        dp[-1] = True
        for i in range(N-2, -1, -1):
            for j in range(1, nums[i]+1):
                if dp[i+j]:
                    dp[i] = True
                    break # Prune the extra routes. Otherwise might have out of
                    # index as well as more redundancies.
        return dp[0]

    def canJump_4(self, nums: List[int]) -> bool:
        n = len(nums)
        lastposition = n - 1
        for i in range(n - 2, -1, -1):
            if i + nums[i] >= lastposition:
                lastposition = i
        return lastposition == 0

    def canJump_5(self, nums: List[int]) -> bool:
        # Very similar to backward dp (canJump_dp), with more pruning.
        destination = len(nums) - 1
        source = destination - 1 # One step backwards each time
        
        while source >= 0: # Ending condition: source == 0
            if source + nums[source] >= destination:
                destination = source
                source -= 1 # One step each to far away if not succeed
            else:
                source -= 1 # However it goes, decrements source by one 
                # each to get to the ending condition
                
        return destination == 0