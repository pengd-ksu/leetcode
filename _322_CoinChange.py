class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for c in coins:
            for i in range(c, amount + 1):
                dp[i] = min(dp[i], dp[i-c] + 1)
                
        return dp[amount] if dp[amount] != float('inf') else -1

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        q = deque([(amount, 0)])
        seen = set()
        seen.add(amount)
        while q:
            accum_amount, num_coins = q.popleft()
            if accum_amount == 0:
                    return num_coins
            for coin in coins:
                if accum_amount - coin >= 0 and accum_amount - coin not in seen:
                    q.append((accum_amount - coin, num_coins + 1))
                    seen.add(accum_amount - coin)

        return -1

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #Can't pass time limit
        coins.sort(reverse = True)
        ans = float('inf')
        def dfs(coinCount, amountRemain, startIdx):
            nonlocal ans
            if amountRemain == 0:
                ans = min(ans, coinCount)
                return
            elif amountRemain < 0:
                return
            else:
                for i in range(startIdx, len(coins)):
                    noLess = ans - coinCount
                    if noLess * coins[i] > amountRemain:
                        dfs(coinCount+1, amountRemain-coins[i], i)
        dfs(0, amount, 0)
        return -1 if ans == float('inf') else ans

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        rs = [amount+1] * (amount+1)
        rs[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if i >= c:
                    rs[i] = min(rs[i], rs[i-c] + 1)

        if rs[amount] == amount+1:
            return -1
        print(rs)
        return rs[amount]