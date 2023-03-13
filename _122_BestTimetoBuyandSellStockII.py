from typing import List
from pytest import mark

class Solution:
    def maxProfit(prices: List[int]) -> int:
        #draw a graph of the changing prices. Alway buy before rising,
        #and selling before falling
        max_profit = 0
        n = len(prices)
        flag = False#Whether there's stock in hands
        for i in range(n):
            if not flag:
                if i + 1 <= n - 1 and prices[i + 1] <= prices[i]:
                    continue
                else:
                    buy_price = prices[i]#Even if 
                    flag = True
            else:
                if i + 1 <= n - 1 and prices[i + 1] <= prices[i]:
                    max_profit += (prices[i] - buy_price)
                    flag = False
                elif i == n - 1:
                    max_profit += (prices[i] - buy_price)
                else:
                    continue
        return max_profit

    def maxProfit_simple(prices: List[int]) -> int:
        maxprofit = 0
        n = len(prices)
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                maxprofit += prices[i] - prices[i - 1]
        return max_profit

    def maxProfit_2(prices: List[int]) -> int:
        i = 0
        valley = prices[0]
        peak = prices[0]
        maxprofit = 0
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]
            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]
            maxprofit += peak - valley
        return maxprofit
        

@mark.parametrize('prices, expected', [
        ([7,1,5,3,6,4], 7),
        ([1,2,3,4,5], 4),
        ([7,6,4,3,1], 0),
    ])

def test_maxProfit(prices, expected):
    ans = Solution.maxProfit(prices)
    assert ans == expected