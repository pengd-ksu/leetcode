class Solution:# Official approach 2. Optimized.
    def hammingWeight(self, n: int) -> int:
        # Key: n & (n-1) will flip the least significant 1 to 0, and keep other ones untouched:110100 & 110011 = 110000
        total = 0
        while n:
            total += 1
            n &= (n - 1)
        return total

class Solution:
    def hammingWeight(self, n: int) -> int:
        hw = 0
        for i in range(32):
            hw += (n >> i) & 1
        return hw

class Solution:
    def hammingWeight(self, n: int) -> int:
        ones = 0
        cp = n
        for _ in range(32):
            ones += cp & 1
            cp >>= 1
        return ones