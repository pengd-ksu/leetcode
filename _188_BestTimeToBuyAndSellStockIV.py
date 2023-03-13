class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) <= 1 or k == 0:
            return 0
        #k transactions include 2 * k of buying and selling together.
        #don't use states[0] actually
        states = [0] + [float('-inf') for i in range(2 * k)]
        states[1] = -prices[0]#The first can only buy in, which means spend prices[0]
        #odd index for buying and even for selling
        for i in range(1, len(prices)):
            for j in range(k):
                states[2 * j + 1] = max(states[2 * j + 1], states[2 * j] - prices[i])
                states[2 * j + 2] = max(states[2 * j + 2], states[2 * j + 1] + prices[i])
        return max(0, states[-1])

    def maxProfit_DP(self, k: int, prices: List[int]) -> int:
        if k == 0 or len(prices) == 0:
            return 0

        min_price, profit = [float('inf')] * k, [float('-inf')] * k
        for price in prices:
            min_price[0] = min(min_price[0], price)
            profit[0] = max(profit[0], price - min_price[0])
            for i in range(1, k):
                min_price[i] = min(min_price[i], price - profit[i-1])
                profit[i] = max(profit[i], price - min_price[i])
        
        return profit[k-1]

    def maxProfit_DP2(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        sell = [0 for i in range(k+1)]
        buy = [float('-inf') for i in range(k+1)]
        for i in range(n):
            for j in range(k, 0, -1):
                sell[j] = max(sell[j], prices[i] + buy[j])
                buy[j] = max(buy[j], sell[j-1] - prices[i])
        return sell[k]