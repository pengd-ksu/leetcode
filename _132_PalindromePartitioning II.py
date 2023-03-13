from typing import List
from pytest import mark

class Solution:
    def minCut_brute(self, s: str) -> int:
        #Not sure if this is right, because it doesn't pass all the tests due to
        #time limit
        minC = float('inf')
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        def dfs(s, start, currentList, dp):
        #https://stackoverflow.com/questions/18002794/local-variable-referenced-before-assignment
        #When Python parses the body of a function definition and encounters an assignment such as feed = ... Python interprets feed as a local variable by default
            nonlocal minC
            nonlocal n
            if start >= n:
                minC = min(minC, len(list(currentList)) - 1)
                return
            for end in range(start, n):
                if s[start] == s[end] and (end - start <= 2 or dp[start + 1][end - 1]):
                    dp[start][end] = True
                    currentList.append(s[start: end + 1])
                    dfs(s, end + 1, currentList, dp)
                    currentList.pop()

        dfs(s, 0, [], dp)
        return minC

    def minCut_brute2(self, s: str) -> int:
        #Not sure if this is right, because it doesn't pass all the tests due to
        #time limit
        res = sys.maxsize
        @cache
        def backTracking(curr_path, start):
            nonlocal res
            if start == len(s):
                return curr_path - 1
            for i in range(start + 1, len(s) + 1):
                sub_string = s[start : i]
                if sub_string == sub_string[::-1]:
                    res = min(res, backTracking(curr_path + 1, i))
            return res
        L = backTracking(0, 0)
        return L

    def minCut_3(self, s: str) -> int:
        n = len(s)
        dp = [1] * n # start with 1 because a character can be a palindrome itself
        palindrome = [[False] * n for _ in range(n)]
        
        # Step 1: Build the palindrome map
        # to check whether substring from start - end is palindrome or not
        # Intuition: substring from start -> end is palindrome if character[start] == character[end] and substring from start + 1 -> end - 1 is also palindrome
        for start in reversed(range(n)):
            for end in range(start,n):
                if s[start] == s[end] and (end-start <= 2 or palindrome[start+1][end-1]):
                    palindrome[start][end] = True
        
        # Step 2: intuition: find min number of palindromes can be made at index start
        # if substring start -> end is a palindrome => substring starts at end+1 also palindrome
        # => find all substrings start with `start` index (start, start -> start,n-1) and get the min number of palindroms can be made
        # the final output is at i == 0
        # The problem asks about min cut => only cuts between palindromes. i.e: have n palindromes => cuts = n-1
        for start in reversed(range(n)):
            res = float('inf')
            for end in range(start,n):
                if palindrome[start][end]:
                    if end < n-1:
                        res = min(res, 1 + dp[end+1])
                    else: # edge case: end of the string, i.e: "aaaaaa"
                        res = 1
            dp[start] = res
            
        return dp[0]-1

    def minCut_4(self, s: str) -> int:
        def expand_from_center(s, start, end, dp):
            while start >= 0 and end < len(s) and s[start] == s[end]:
                cuts = 0 if start == 0 else (dp[start-1] + 1)
                # dp table is to track min cuts so far
                # for substring start-end, the min cuts at end of current substring will be min cuts at end of previous substring + 1
                dp[end] = min(dp[end], cuts)
                start -= 1
                end += 1
                
        n = len(s)
        dp = [0] * n 
        # to track the min possible cuts so far, 
        # start with default values that are equal to number of characters so far.
        # i.e: "abc" dp = [0,1,2] -> 0 cut to cut "a", 1 cut to cut "ab", 2 cuts to cut "abc"
        
        for i in range(n):
            dp[i] = i
            
        for i in range(n):
            expand_from_center(s, i, i, dp)
            expand_from_center(s, i, i+1, dp)
            
        return dp[n-1]

    def minCut_5(self, s: str) -> int:
        n = len(s)
        palindrome = [[False] * n for _ in range(n)]
        for start in reversed(range(n)):
            for end in range(start,n):
                if s[start] == s[end] and (end-start <= 2 or palindrome[start+1][end-1]):
                    palindrome[start][end] = True
        f = [float('inf')] * n
        for i in range(n):
            if palindrome[0][i]:
                f[i] = 0
            else:
                for j in range(i):
                    if palindrome[j+1][i]:
                        f[i] = min(f[i], f[j] + 1)
        return f[n-1]

@mark.parametrize('s, expected', [
        ("aab", [["a","a","b"],["aa","b"]]),
        ("a", [["a"]]),
])

def test_partition(s, expected):
    ans = Solution.partition(s)
    assert ans == expected
