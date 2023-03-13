from typing import List

from pytest import mark

class Solution:
    def combine_recur_backtrack(n: int, k: int) -> List[List[int]]:
        ans = []
        def recurse_backtrack(start: int, combo: List[int]) -> None:
            if len(combo) == k:
                ans.append(list(combo))
            else:
                for i in range(start, n+1):
                    combo.append(i)
                    recurse_backtrack(i+1, combo)
                    combo.pop()
        recurse_backtrack(1, [])
        return ans

    def combine(self, n: int, k: int) -> List[List[int]]:
        #if n == 1:# No need
        #    return [[1]]
        
        ans = []
        nlist = [i for i in range(1, n + 1)]
        
        def backtrack(path, startIdx):
            if len(path) == k:# This must come first, in case append the last ele.
                ans.append(path)
                return
            if startIdx == n + 1 or len(path) > k:
                return
            for i in range(startIdx, len(nlist)):
                backtrack(path + [nlist[i]], i + 1)
                
        backtrack([], 0)
        
        return ans

    def combine_recur(self, n: int, k: int) -> List[List[int]]:
        if k == 0:
            return [[]]
        return [pre + [i] for i in range(k, n + 1) for pre in self.combine(i-1, k-1)]

    def combine_iter(self, n: int, k: int) -> List[List[int]]:
        combs = [[]]
        for _ in range(k):
            combs = [[i] + c for c in combs for i in range(1, c[0] if c else n+1)]
        return combs

    def combine_reduce(self, n: int, k: int) -> List[List[int]]:
        return reduce(lambda C, _: [[i]+c for c in C for i in range(1, c[0] if c else n+1)], range(k), [[]])

@mark.parametrize('n, k, expected', [
        (4, 2, [[1,2], [1,3], [1,4], [2,3], [2,4], [3,4],]),
        (1, 1, [[1]]),
    ])

def test_combine(n, k, expected):
    ans = Solution.combine_recur_backtrack(n, k)
    assert ans == expected