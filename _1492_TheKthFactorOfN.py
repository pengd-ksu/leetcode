class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        import math
        maxf = int(math.sqrt(n))
        ans = []
        for i in range(1, maxf+1):
            if n % i == 0:
                j = n // i
                if i != j:
                    ans.extend([i,j])
                else:
                    ans.append(i)
        if len(ans) < k:
            return -1
        ans.sort()
        return ans[k-1]