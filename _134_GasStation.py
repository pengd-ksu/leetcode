from typing import List
from pytest import mark

class Solution:
    def canCompleteCircuit_brute(gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for i in range(n):
            step = n
            index = i
            hasGas = 0
            needGas = cost[index]
            while step:
                hasGas += gas[index]
                if hasGas >= cost[index]:
                    hasGas -= cost[index]
                    step -= 1
                    index = (index + 1) % n
                else:
                    break
            if step == 0 and index == i:
                return index
        return -1

    def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
        start = surplus = deficit = 0
        for i in range(len(gas)):
            surplus += gas[i] - cost[i]
            if surplus < 0:
                start = i + 1
                deficit += surplus
                surplus = 0
        if surplus + deficit >= 0:
            return start
        return -1

@mark.parametrize('gas, cost, expected', [
        ([1,2,3,4,5], [3,4,5,1,2], 3),
        ([2,3,4], [3,4,3], -1),
    ])

def test_canCompleteCircuit(gas, cost, expected):
    ans = Solution.canCompleteCircuit(gas, cost)
    assert ans == expected