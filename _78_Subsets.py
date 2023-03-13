from typing import List
from pytest import mark

class Solution:
    def subsets_combo(nums: List[int]) -> List[List[int]]:
        ans = []
        ans.append([])
        n = len(nums)
        def recurse(combo: List[int], nums: List[int], start: int, k: int) -> None:
            if len(combo) == k:
                ans.append(list(combo))
            else:
                for i in range(start, len(nums)):
                    combo.append(nums[i])
                    recurse(combo, nums, i + 1, k)
                    combo.pop()
        for k in range(1, len(nums)+1):
            recurse([], nums, 0, k)
        return ans

    #Solution2 will not pass, because answers generated in different order
    def subsets(nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(subset=[], idx=0):
            if idx == len(nums):
                ans.append(subset)
            else:#either include the current ele or not. Keep going.
                backtrack(subset, idx+1)
                backtrack(subset+[nums[idx]], idx+1)
        backtrack()
        return ans

    def subsets_2(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def choice(nums, idx, path):
            if idx == len(nums):
                ans.append(list(path))
                return
            choice(nums, idx+1, path+[nums[idx]])
            choice(nums, idx+1, path)
            
        choice(nums, 0, [])
        return ans

    def subsets_3(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for n in nums:
            subsets += [s + [n] for s in subsets]
            
        return subsets

    def subsets_4(self, nums: List[int]) -> List[List[int]]:
        return reduce(lambda subsets, n: subsets + [s+[n] for s in subsets], nums, [[]])

    def subsets_dfs(self, nums: List[int]) -> List[List[int]]:
        ret = []
        self.dfs(nums, [], ret)
        return ret
    
    def dfs(self, nums, path, ret):
        ret.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i+1:], path+[nums[i]], ret)

@mark.parametrize('nums, expected', [
        ([1,2,3], [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]),
        ([0], [[],[0]]),
    ])

def test_subsets(nums, expected):
    ans1 = Solution.subsets_combo(nums)
    assert ans1 == expected