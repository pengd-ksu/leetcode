from typing import List
import functools
from pytest import mark

class Solution:

    memo = {}
    @functools.cache
    def numTrees(self, n: int) -> int:
        if n == 0:
            self.memo[n] = 1
        elif n == 1:
            self.memo[n] = 1
        elif n == 2:
            self.memo[n] = 2
        else:
            self.memo[n] = 0
            for i in range(n):
                self.memo[n] += self.numTrees(i) * self.numTrees(n-i-1)
        return self.memo[n]

    def numTrees_2(self, n: int) -> int:
        # Choose a node as root ranging [1,n] (inclusive), then it depends the product of 
        # left subtree and right subtree
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i-j-1]
        return dp[n]

    def numTrees_3(self, n: int) -> int:
        # Catlan number. Check https://en.wikipedia.org/wiki/Catalan_number and 
        # MIT 6.006 lecture 11 Spring 2011
        return int(math.factorial(2*n)/(math.factorial(n)*math.factorial(n+1)))

    @functools.cache
    def numTrees_DC_Cache(n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        result = 0
        for i in range(n):#node (i+1) as the root node.
            result += max(Solution.numTrees_DC_Cache(i), 1) * max(1,Solution.numTrees_DC_Cache(n-i-1))
        return result

    #due to BST's traits, right subnode is larger than left. Result will be 
    #left distinct subtrees * right distict subtress

    def numTrees_cache(n: int) -> int:
        cache = {}

        def dp(start: int, end: int) -> int:
            if end <= start:
                return 1#base condition in dynamic programming
            elif (start, end) in cache.keys():
                return cache[(start, end)]
            result = 0
            for i in range(end-start+1):
                result += dp(start, start+i-1) * dp(start+i+1, end)
            cache[(start, end)] = result
            return result

        return dp(1, n)

@mark.parametrize('n, expected', [
    (3, 5),
    (1, 1),
])

def test_numTrees(n, expected):
    ans1 = Solution.numTrees_DC_Cache(n)
    ans2 = Solution.numTrees_cache(n)
    assert ans1 == expected
    assert ans2 == expected