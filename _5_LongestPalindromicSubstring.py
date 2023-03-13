class Solution:
    def longestPalindrome(self, s: str) -> str:
        #Can't pass the longest test. O(n^2)
        longest = s[0]
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    if j - i == 1 or dp[i+1][j-1] == True:
                        dp[i][j] = True
                        if len(longest) < len(s[i:j+1]):
                            longest = s[i:j+1]
        return longest

    def longestPalindrome_2(self, s: str) -> str:
        # get the longest palindrome, l, r are the middle indexes   
        # from inner to outer
        def helper(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1; r += 1
            return s[l+1:r]
        
        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res

    def longestPalindrome_3(self, s: str) -> str:
        #Can't pass. O(n^2)
        if not s:
            return s#Null case
        ans = s[0]
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
        for i in range(1, len(s)):
            for j in range(i):
                if s[i] == s[j]:
                    if i - j == 1 or dp[j + 1][i - 1] == True:#j+1 < i-1, dp always False
                        dp[j][i] = True
                        if len(ans) < i - j + 1:
                            ans = s[j: i + 1]
        
        return ans

    def longestPalindrome_4(self, s: str) -> str:
        def expandPalin(s: str, l: int, r: int) -> str:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1: r]#In case even the base case doesn't pass. If passed in an pair, it will return ''. If passed a single letter, will return the original letter and it can't expand at all
        
        ans = ''
        for idx in range(len(s)):
            odd = expandPalin(s, idx, idx)
            if len(odd) > len(ans):
                ans = odd
            even = expandPalin(s, idx, idx + 1)
            if len(even) > len(ans):
                ans = even
        return ans