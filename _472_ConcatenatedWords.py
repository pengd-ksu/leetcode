class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key = len)
        
        def wordbreak(s, wordDict):
            if not wordDict:
                return False
            dp = [False] * (len(s) + 1)
            dp[0] = True
            for i in range(1, len(s) + 1):
                for j in range(i):
                    if s[j:i] in wordDict and dp[j]:
                        dp[i] = True
            return dp[-1]
        
        ans = []
        wordDict = set()
        for w in words:
            if wordbreak(w, wordDict):
                ans.append(w)
            wordDict.add(w)
            
        return ans

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        d = set(words)
        
        def dfs(word):
            for i in range(1, len(word)):
            # Can't be len(word)+1, in the test case, some of them contains '', 
            # which makes it possible that every word would be its own 
            # prefix(suffix as '' is also in the words list)
                prefix = word[:i]
                suffix = word[i:]
                
                if prefix in d and suffix in d:
                    return True
                if prefix in d and dfs(suffix):
                    return True
            return False
        
        ans = []
        for w in words:
            if dfs(w):
                ans.append(w)
                
        return ans