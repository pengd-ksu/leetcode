class Solution:
    # This could lead to Memory Limit Exceeded. Store too many.
    def __init__(self, w: List[int]):
        self.dice = []
        #self.dic = dict()
        self.count = 0
        for idx, weight in enumerate(w):
            self.dice.extend([idx] * weight)
            #dic[weight] = idx

    def pickIndex(self) -> int:
        d = random.randint(0, len(self.dice)-1)
        return self.dice[d]
        
class Solution:
    # This one works. Inspired by:
# https://leetcode.com/problems/random-pick-with-weight/discuss/671921/Python-3-simple-solution
    def __init__(self, w: List[int]):
        self.total = sum(w)
        self.weight = w
        for i in range(1, len(self.weight)):
            self.weight[i] += self.weight[i-1]

    def pickIndex(self) -> int:
        d = random.randint(1, self.total)
        flag = True
        idx = -1
        while flag:
            idx += 1
            if d <= self.weight[idx]:
                flag = False
        return idx
        
class Solution:
    def __init__(self, w: List[int]):
        self.cdf = [0]
        for weight in w:
            self.cdf.append(self.cdf[-1] + weight)
            #Since cdf starts with only one 0, cdf[-1] is 0 for first 
            # weight

    def pickIndex(self) -> int:
        rand = random.randint(1, self.cdf[-1])
        idx = bisect.bisect_left(self.cdf, rand)
        return idx - 1

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()