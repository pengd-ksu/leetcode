from typing import List
from pytest import mark

class Solution:
    def maxProfit(prices: List[int]) -> int:
        #Divide array into two parts, before i(included) and after i
        #You can only sell after buying, forward and backward are different to
        #reflect that trait. Also one trasaction at a time.
        #forward[i] = max(forward[i-1], prices[i]-lowestprice[:i+1])
        #backward[i] = max(backward[i+1], highestprice[i+1:]-prices[i+1])
        n = len(prices)
        if n <= 1:
            return 0
        
        forward = [0] * n
        backward = [0] * n
        lowestPrice = prices[0]
        for i in range(1, n):
            forward[i] = max(forward[i - 1], prices[i] - lowestPrice)
            lowestPrice = min(lowestPrice, prices[i])
        
        highestPrice = prices[-1]
        for j in range(n - 2, 0, -1):
            backward[j] = max(backward[j + 1], highestPrice - prices[j])
            highestPrice = max(highestPrice, prices[j])
            
        maxprofit = 0
        for z in range(n):
            maxprofit = max(maxprofit, forward[z] + backward[z])#Could sell then buy on the same day
            
        return maxprofit
        

@mark.parametrize('prices, expected', [
        ([3,3,5,0,0,3,1,4], 6),
        ([1,2,3,4,5], 4),
        ([7,6,4,3,1], 0),
        ([1], 0),
    ])

def test_maxProfit(prices, expected):
    ans = Solution.maxProfit(prices)
    assert ans == expected