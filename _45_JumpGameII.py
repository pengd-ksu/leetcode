class Solution:
    def jump(self, nums: List[int]) -> int:
        # "You can assume that you can always reach the last index."
        n = len(nums)
        dp = [math.inf for i in range(n)] #store minimum jumps to each index
        dp[0] = 0 #because it's the initial position, so it needs zero jumps.
        for i in range(n):
            for j in range(i, min((i + nums[i] + 1), n)):
                dp[j] = min(dp[i] + 1, dp[j])
                
        return dp[n - 1]

    def jump_2(self, nums: List[int]) -> int:
        # Slightly improvement to jump_1
        dp = [float('inf')] * len(nums)
        dp[0] = 0 # Starting position doesn't need any move
        for i in range(len(nums)):
            for j in range(i + 1, min(len(nums), i + nums[i] + 1)): # No 
                # move taken if nums[i] == 0 here
                dp[j] = min(dp[j], dp[i] + 1)
        print(dp)
        return dp[-1]

    def jump_3(self, nums: List[int]) -> int:
        # It's from: 
        #https://leetcode.com/problems/jump-game-ii/discuss/18019/10-lines-C%2B%2B-(16ms)-Python-BFS-Solutions-with-Explanations
        # "You can assume that you can always reach the last index."
        n = len(nums)
        # Keep a range of [start, end] inclusive from both ends.
        start, end = 0, 0
        steps = 0
        while end < n - 1:
            steps += 1
            # We could assume every nums[i] must make a move, so we can set 
            # end+1 as basic move
            maxend = end + 1
            for i in range(start, end + 1):
                #if steps >= n - 1: # Don't understand why take this step.
                    #return steps
                maxend = max(maxend, i + nums[i])
            # It's guaranteed to move, very important!
            start = end + 1
            end = maxend
        return steps