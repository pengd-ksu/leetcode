class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        N = len(nums)
        nums.sort()

        pow2 = [1]
        for i in range(1, N):
            pow2.append(pow2[-1] * 2 % MOD)

        ans = 0
        for i, x in enumerate(nums):
            ans = (ans + (pow2[i] - pow2[N-1-i]) * x) % MOD
        return ans

"""
From https://leetcode.com/problems/sum-of-subsequence-widths/discuss/161267/JavaC%2B%2BPython-Sort-and-One-Pass

Explanation
The order in initial arrays doesn't matter,
my first intuition is to sort the array.

For each number A[i]:

There are i smaller numbers,
so there are 2 ^ i sequences in which A[i] is maximum.
we should do res += A[i] * 2^i

There are n - i - 1 bigger numbers,
so there are 2 ^ (n - i - 1) sequences in which A[i] is minimum.
we should do res -= A[i] * 2^(n - i - 1)

Done.
"""
class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        return sum(((1 << i) - (1 << len(nums) - i - 1)) * a \
            for i, a in enumerate(sorted(nums))) % (10**9 + 7)