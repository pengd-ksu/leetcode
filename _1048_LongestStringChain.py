class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # Key: consider delete one letter and check if the rest exits
        # dfs with memoization
        memo = {}#what should be the key?
        check = set(words)
        ans = 0
        
        def dfs(current_word: str) -> int:# what to return?
            if current_word in memo.keys():
                return memo[current_word]
            maxlen = 1
            # check memo?
            for i in range(len(current_word)):
                new_word = current_word[:i] + current_word[i+1:]
                if new_word in check:
                    maxlen = max(maxlen, 1 + dfs(new_word))
            memo[current_word] = maxlen
            return maxlen
        
        for current_word in words:
            ans = max(ans, dfs(current_word))
        
        return ans


class Solution: # Bottom-up
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        result = 1

        for word in sorted(words, key=len):
            dp[word] = 1

            for i in range(len(word)):
                prev = word[:i] + word[i + 1:]

                if prev in dp:
                    dp[word] = max(dp[prev] + 1, dp[word])
                    result = max(result, dp[word])

        return result

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        for w in sorted(words, key=len):
            dp[w] = max(dp.get(w[:i] + w[i + 1:], 0) + 1 for i in range(len(w)))
        return max(dp.values())
