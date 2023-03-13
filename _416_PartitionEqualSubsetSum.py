class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        goal = sum(nums) // 2
        dp = [True] + [False] * goal
        for n in nums:
            for i in range(goal, n - 1, -1):
                dp[i] = dp[i] or dp[i - n]
        return dp[goal]

class Solution: # Official Approach 1: brute force. Time Limit Exceed
    def canPartition(self, nums: List[int]) -> bool:
        def dfs(nums: List[int], n: int, subset_sum: int) -> bool:
            if subset_sum == 0:
                return True
            if n == 0 or subset_sum < 0:
                return False
            return dfs(nums, n - 1, subset_sum - nums[n - 1]) or \
        dfs(nums, n - 1, subset_sum)
        
        total_sum = sum(nums)
        
        if total_sum % 2 != 0:
            return False
        
        subset_sum = total_sum // 2
        n = len(nums)
        return dfs(nums, n - 1, subset_sum)

class Solution: # Approach 2: Top Down Dynamic Programming - Memoization
    def canPartition(self, nums: List[int]) -> bool:
        @lru_cache(maxsize=None)
        def dfs(nums: Tuple[int], n: int, subset_sum: int) -> bool:
            # Base cases
            if subset_sum == 0:
                return True
            if n == 0 or subset_sum < 0:
                return False
            result = (dfs(nums, n - 1, subset_sum - nums[n - 1])
                    or dfs(nums, n - 1, subset_sum))
            return result

        # find sum of array elements
        total_sum = sum(nums)

        # if total_sum is odd, it cannot be partitioned into equal sum subsets
        if total_sum % 2 != 0:
            return False

        subset_sum = total_sum // 2
        n = len(nums)
        return dfs(tuple(nums), n - 1, subset_sum)

class Solution: # Approach 3: Bottom Up Dynamic Programming
    def canPartition(self, nums: List[int]) -> bool:
        # find sum of array elements
        total_sum = sum(nums)

        # if total_sum is odd, it cannot be partitioned into equal sum subsets
        if total_sum % 2 != 0:
            return False
        subset_sum = total_sum // 2
        n = len(nums)

        # construct a dp table of size (n+1) x (subset_sum + 1)
        dp = [[False] * (subset_sum + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            curr = nums[i - 1]
            for j in range(subset_sum + 1):
                if j < curr:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - curr]
        return dp[n][subset_sum]

class Solution: # Approach 4: Optimised Dynamic Programming - Using 1D Array
    def canPartition(self, nums: List[int]) -> bool:
        # find sum of array elements
        total_sum = sum(nums)

        # if total_sum is odd, it cannot be partitioned into equal sum subsets
        if total_sum % 2 != 0:
            return False
        subset_sum = total_sum // 2

        # construct a dp table of size (subset_sum + 1)
        dp = [False] * (subset_sum + 1)
        dp[0] = True
        for curr in nums:
            for j in range(subset_sum, curr - 1, -1):
                dp[j] = dp[j] or dp[j - curr]

        return dp[subset_sum]