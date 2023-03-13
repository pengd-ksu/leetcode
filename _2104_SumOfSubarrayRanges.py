class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            l, r = nums[i], nums[i]
            for j in range(i, len(nums)):
                l = min(l, nums[j])
                r = max(r, nums[j])
                ans += r - l
        return ans

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        inf = float('inf')
        A = [-inf] + nums + [-inf]
        s = []
        for i, x in enumerate(A):
            #s is a monotonic increasing stack
            #A[j] is larger than A[k] and smaller than x
            #i and j is one more than real index, but it's fine
            while s and A[s[-1]] > x:
                j = s.pop()
                k = s[-1]
                res -= A[j] * (i - j) * (j - k)
            s.append(i)
            
        A = [inf] + nums + [inf]
        s = []
        for i, x in enumerate(A):
            while s and A[s[-1]] < x:
                j = s.pop()#j is the previous maximum
                k = s[-1]
                res += A[j] * (i - j) * (j - k)
            s.append(i)
        return res