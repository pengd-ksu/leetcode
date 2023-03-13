class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # Compare every bit to see if they are the same.
        ans = 0
        big = max(x, y)
        while big:
            ans += (x & 1) ^ (y & 1)# 1 to mask off the other bits
            x >>= 1
            y >>= 1
            big >>= 1
        return ans

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        distance = 0
        while xor:
            if xor & 1:
                distance += 1
            xor >>= 1
        return distance

class Solution: # Brian Kernighan's bit counting algorithm
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        distance = 0
        while xor:
            distance += 1
            xor = xor & (xor - 1)# clear the bits on right of least significant bit
        return distance