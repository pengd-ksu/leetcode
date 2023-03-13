class Solution:# Based on 191 Hammingweight
    def countBits(self, n: int) -> List[int]:
        def pop_count(n: int) -> int:
            count = 0
            while n:
                count += 1
                n &= n - 1
            return count
        
        ans = [0] * (n + 1)
        for x in range(n + 1):
            ans[x] = pop_count(x)
        
        return ans

class Solution: # Approach 2: DP + Most Significant Bit
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        x = 0
        b = 1
        while b <= n:
            while x < b and x + b <= n:
                ans[x + b] = ans[x] + 1
                x += 1
            x = 0
            b <<= 1
        
        return ans

class Solution: # Approach 3: DP + Least Significant Bit
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for x in range(1, n + 1):
            # x // 2 is x >> 1 and x % 2 is x & 1
            ans[x] = ans[x >> 1] + (x & 1)
        return ans

class Solution: # Approach 4: DP + Last Set Bit
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for x in range(1, n + 1):
            ans[x] = ans[x & (x - 1)] + 1
        return ans