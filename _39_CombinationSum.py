from typing import List

class Solution:
    def combinationSum_dfs(self, candidates, target):
        ret = []
        self.dfs(candidates, target, [], ret)
        return ret
    
    def dfs(self, nums, target, path, ret):
        if target < 0:
            return 
        if target == 0:
            ret.append(path)
            return 
        for i in range(len(nums)):
            self.dfs(nums[i:], target-nums[i], path+[nums[i]], ret)

    def combinationSum_dp1(candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        dp = [None] + [set() for i in range(target)]
        for cand in candidates:
            if cand > target:
                break
            dp[cand].add((cand,))

            for i in range(1, target-cand+1):
                dp[cand+i] |= {comb + (cand,) for comb in dp[i]}

        return dp[target]

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def combine(path, total, idx):
            if total == target:
                ans.append(path)
                return
            if idx >= len(candidates):
                return
            if total > target:
                return
            combine(path+[candidates[idx]], total+candidates[idx], idx)
            combine(path, total, idx+1)
                
        combine([], 0, 0)
        return ans

    def combinationSum_dp2(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]
        for can in candidates:
            for i in range(target + 1):
                if i == can:
                    dp[i].append([i])
                if i > can:
                    for comb in dp[i-can]:
                        dp[i].append(comb + [can])
        return dp[target]

    def combinationSum_bfs(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        from collections import deque
        queue = deque()
        queue.append((target, [], 0))#aim, path, and starting index
        while queue:
            curTarget, curPath, curIdx = queue.popleft()
            for i in range(curIdx, len(candidates)):
                newTarget = curTarget - candidates[i]
                if newTarget == 0:
                    ans.append(curPath + [candidates[i]])
                if newTarget > 0:
                    queue.append((newTarget, curPath + [candidates[i]], i))
        return ans

    def combinationSum_backtrack(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def combine(curPath, curSum, startIdx):
            if curSum == target:
                ans.append(curPath)
                return
            if curSum > target:
                return
            for i in range(startIdx, len(candidates)):
                combine(curPath + [candidates[i]], curSum + candidates[i], i)
                
        combine([], 0, 0)
        return ans

if __name__ == '__main__':
    #print(combinationSum_dp(candidates = [2,3,6,7], target = 7))
    print(Solution.combinationSum_dp(candidates = [2,3,5], target = 8))
    #print(combinationSum_dp(candidates = [1,5,10,25,50], target = 100)) # Test effeciency