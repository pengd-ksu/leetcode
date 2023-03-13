class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #brute force. Can't pass long tests.
        count = 0
        def findtotal(arr, total):
            nonlocal count
            if not arr and total == target:
                count += 1
                return
            elif not arr:
                return
            elif arr:
                findtotal(arr[1:], total+arr[0])
                findtotal(arr[1:], total-arr[0])
        
        findtotal(nums, 0)
        return count

    def findTargetSumWays_2(self, nums: List[int], target: int) -> int:
        def dfs(cur, i, d = {}):
            if i < len(nums) and (i, cur) not in d: 
                d[(i, cur)] = dfs(cur + nums[i], i + 1) + dfs(cur - nums[i], i + 1)
            return d.get((i, cur), int(cur == target))
        
        return dfs(0, 0)

    def findTargetSumWays_3(self, nums: List[int], target: int) -> int:     
        dic = defaultdict(int)
        
        def dfs(index=0, total=0):          
            key = (index, total)
            
            if key not in dic:
                if index == len(nums):                    
                    return 1 if total == target else 0
                else:
                    dic[key] = dfs(index+1, total + nums[index]) + dfs(index+1, total - nums[index])                    
                        
            return dic[key]                                                             
                
        return dfs()

    def findTargetSumWays_4(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        dp = [[0 for _ in range(2 * total + 1)] for _ in range(len(nums))]
        dp[0][nums[0] + total] += 1
        dp[0][-nums[0] + total] += 1
        
        for i in range(1, len(nums)):
            for j in range(total * 2):
                if dp[i-1][s + total] > 0:
                    dp[i][s + nums[i] + total] += dp[i - 1][s + total]
                    dp[i][s - nums[i] + total] += dp[i - 1][s + total]
                    
        return 0 if abs(s) > total else dp[len(nums) - 1][s + total]

    def findTargetSumWays_5(self, nums, S):
        #Can't pass long tests. Need pruning
        index = len(nums) - 1
        curr_sum = 0
        return self.dp1(nums, S, index, curr_sum)

    def dp1(self, nums, target, index, curr_sum):
        # Base Cases
        if index < 0 and curr_sum == target:
            return 1
        if index < 0:
            return 0 

        # Decisions
        positive = self.dp1(nums, target, index-1, curr_sum + nums[index])
        negative = self.dp1(nums, target, index-1, curr_sum + -nums[index])

        return positive + negative

    def findTargetSumWays_6(self, nums, S):
        index = len(nums) - 1
        curr_sum = 0
        self.memo = {}
        return self.dp2(nums, S, index, curr_sum)
        
    def dp2(self, nums, target, index, curr_sum):
        if (index, curr_sum) in self.memo:
            return self.memo[(index, curr_sum)]
        if index < 0 and curr_sum == target:
            return 1
        elif index < 0:
            return 0
        positive = self.dp2(nums, target, index - 1, curr_sum + nums[index])
        negative = self.dp2(nums, target, index - 1, curr_sum - nums[index])
        self.memo[(index, curr_sum)] = positive + negative
        return self.memo[(index, curr_sum)]