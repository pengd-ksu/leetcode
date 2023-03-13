from typing import List
from pytest import mark

class Solution:
    #Not sure if the brute force method is true or not.
    def wordBreak_brute(self, s: str, wordDict: List[str]) -> bool:
        result = []
        def helper(s, wordDict, result):
            for i in range(len(s)):
                if s[:i + 1] in wordDict:
                    if i + 1 == len(s):
                        result.append(True)
                    else:
                        helper(s[i + 1:], wordDict, result)
                else:
                    if i + 1 == len(s):
                        result.append(False)
                    
        helper(s, wordDict, result)
        return any(result)

    def wordBreak_dp(s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)#index 0 means null, which is set to be True
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i + 1):
                if dp[j] and (s[j:i] in wordSet):
                    dp[i] = True#dp[i] is one step ahead of s[i]
        return dp[n]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Brute force. Time Limit Exceeded.
        wordSet = set(wordDict)
        result = False
        if not s:
            return True
        for i in range(1, len(s) + 1):
            if s[:i] in wordSet:
                result = result or self.wordBreak(s[i:], wordDict)
        return result

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        # dp[i] means s[:i+1] can be segmented into words in the wordDicts 
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break # Prune
        return dp[-1]

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ok = [True]
        for i in range(1, len(s) + 1):
            ok += any(ok[j] and s[j:i] in wordDict for j in range(i)), # The comma creates a tuple
        return ok[-1]

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        import collections
        queue = collections.deque()
        queue.append(s)
        seen = set()
        while queue:
            s = queue.popleft()# popleft() = BFS ; pop() = DFS
            for word in wordDict:
                if s.startswith(word):
                    new_str = s[len(word):]
                    if new_str == '':
                        return True
                    if new_str not in seen:
                        seen.add(new_str)
                        queue.append(new_str)
        return False

@mark.parametrize('s, wordDict, expected', [
        ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
            ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]),
        False

    ])

def test_wordBreak(s, wordDict, expected):
    ans = Solution.wordBreak_dp(s, wordDict)
    assert ans == expected