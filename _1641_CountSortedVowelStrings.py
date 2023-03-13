class Solution:
    def countVowelStrings(self, n: int) -> int:
        def countVowelsUntil(num, vowels):
            if num == 1:
                return vowels
            if vowels == 1:
                return 1
            return countVowelsUntil(num - 1, vowels) + countVowelsUntil(num, vowels - 1)
        
        return countVowelsUntil(n, 5)

"""

     a   e   i   o   u
n=1  5   4   3   2   1   a, e, i, o, u
n=2 15  10   6   3   1   aa, ae, ai, ao, au; ee, ei, eo, eu; ii, io, iu; oo, ou; uu
we can see that dp[n][vowels] = dp[n][vowels-1] + dp[n-1][vowels], a has largest vowels
"""
class Solution: # Official approach 1: Backtracking
    def countVowelStrings_dp(self, n: int) -> int:
        def countVowelsUntil(n, vowels):
            if n == 0:
                return 1
            result = 0
            for i in range(vowels, 6):
                result += countVowelsUntil(n - 1, i)
            return result
        
        return countVowelsUntil(n, 1)

class Solution:
    def countVowelStrings_dp_memo(self, n: int) -> int:
        memo = dict()
        def countVowelsUntil(n, vowels):
            if n == 1:
                return vowels
            if vowels == 1:
                return 1
            if (n, vowels) in memo:
                return memo[(n, vowels)]
            result = countVowelsUntil(n - 1, vowels) + countVowelsUntil(n, vowels - 1)
            memo[(n, vowels)] = result
            return result
        
        return countVowelsUntil(n, 5)