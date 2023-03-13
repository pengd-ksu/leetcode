from typing import List
import collections
from pytest import mark

class Solution:
    def maxProfit_1(prices: List[int]) -> int:
        #what if len(prices) == 1?
        n = len(prices)
        dp = [0] * n
        dp[0], min_price = -prices[0], prices[0]
        for i in range(1, n):
            if prices[i - 1] < min_price:
                min_price = prices[i - 1]
            dp[i] = prices[i] - min_price
        max_profit = max(dp)
        if max_profit < 0:
            max_profit = 0
        return max_profit

    def maxProfit_2(prices: List[int]) -> int:
        #what if len(prices) == 1?
        n = len(prices)
        max_profit, min_price = 0, float('inf')
        for i in range(1, n):
            if prices[i - 1] < min_price:
                min_price = prices[i - 1]
            if prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit

    def maxProfit_3(self, prices: List[int]) -> int:
        # There could be several peaks. The maximum profit is definitely to 
        # appear among the peaks. However, it could be possible that the 
        # maximum profits equal to one valley and one or more peaks after the 
        # immediately next peak. But if the next downfall is so low that all 
        # the profits has been cleared, there's no possibility for counting 
        # it. The current profit should be cleared and calculated again.
        maxProfit = 0
        curProfit = 0
        for i in range(len(prices) - 1):
            if curProfit < 0:
                curProfit = 0
            curProfit += prices[i+1] - prices[i]
            if prices[i] < prices[i+1]:
                maxProfit = max(maxProfit, curProfit)
        return maxProfit

    def maxProfit(self, prices: List[int]) -> int:
        #Kadane's algorithm or Maximum subarray problem
        n = len(prices)
        max_so_far, cur = 0, 0
        
        for i in range(1,n):
            cur = max(cur + prices[i] - prices[i-1], 0)
            max_so_far = max(cur, max_so_far)
        return max_so_far

@mark.parametrize('prices, expected', [
        ([7,1,5,3,6,4], 5),#6-1
        ([7,6,4,3,1], 0),
    ])

def test_maxProfit(prices, expected):
    ans = Solution.maxProfit_2(prices)
    assert ans == expected