from typing import List
from pytest import mark

class Solution:
    import collections
    memo = collections.defaultdict(list)
    def partition_1(self, s: str) -> List[List[str]]:
        ans = []
        if not s:
            return [[]]
        if s in self.memo:
            return self.memo[s]
        for i in range(1, len(s) + 1):#len(s)+1, otherwise can't reach the end.
            if s[:i] == s[:i][::-1]:
                for suffix in self.partition(s[i:]):
                    ans.append([s[:i]] + suffix)
        self.memo[s] = ans
        return ans

    def partition_2(self, s: str) -> List[List[str]]:
        return [[s[:i]] + rest for i in range(1, len(s)+1)
                if s[:i] == s[:i][::-1]
                for rest in self.partition(s[i:]) or [[]]]

    def partition_dfs(self, s: str) -> List[List[str]]:
        result = []
        
        def dfs(s, path):
            if not s:
                result.append(path)
                return
            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:
                    dfs(s[i:], path+[s[:i]])
        
        dfs(s, [])
        return result

    def partition_3(s: str) -> List[List[str]]:
        def isPanlindrome(s: str, start: int, end: int) -> bool:
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True#Including condition when start == end
        result = []
        def recurPartition(s: str, output: List[str], start: int) -> None:
            nonlocal result
            if start == len(s):
                result.append(list(output))#Must have a copy of output here.
                return
            for i in range(start, len(s)):
                if isPanlindrome(s, start, i):
                    output.append(s[start:i + 1])
                    recurPartition(s, output, i + 1)
                    output.pop()#preparation for backtrack and next loop
        recurPartition(s, [], 0)
        return result

    def partition_dp(s: str) -> List[List[str]]:
        def dfs(result, s, start, currentList, dp):
            if start >= n:
                result.add(list(currentList))
            for i in range(start, n):
                if s[start] == s[end] and (end - start <= 2 or dp[start + 1][end - 1]):
                    dp[start][end] = True
                    currentList.append(s[start: end + 1])
                    dfs(result, s, end + 1, currentList, dp)
                    currentList.pop()

        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        result = []
        dfs(result, s, 0, [], dp)
        return result


@mark.parametrize('s, expected', [
        ("aab", [["a","a","b"],["aa","b"]]),
        ("a", [["a"]]),
])

def test_partition(s, expected):
    ans = Solution.partition(s)
    assert ans == expected
