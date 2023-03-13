class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Same as Subarray sum equals K with modification. Basic idea is that, 
        # If you get the same remainder again, it means that you've encountered 
        # some sum which is a multiple of K.
        d = dict()
        d[0] = -1# For the case that sums = n*k % k == 0, any such index 
        # minus -1 will be larger than 1. But need to check not the first element
        sums = 0
        
        for i, n in enumerate(nums):
            sums += n
            sums %= k
            if sums in d.keys():
                if not (i == 0 and sums == 0):# Check it's not the first 
                    # that is the multiple of k
                    if i - d[sums] > 1:
                        return True
            else:
                d[sums] = i
        return False