class Solution:
    def longestOnes_1(self, nums: List[int], k: int) -> int:
        left = 0
        ans = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
                if k < 0:
                    while nums[left] != 0:
                        left += 1
                    left += 1
            ans = max(ans, right - left + 1)
        return ans

    def longestOnes_2(self, nums: List[int], k: int) -> int:
        # The secret is, once reached longest contiguous subarray, never 
        # reduce the size even if what is wrapped is an invalid one. 
        # Therefore, in k<0 part, we only extract from left side by one,
        # and never check if k is already nonnegative.
        left = 0
        for right in range(len(nums)):
        # If we included a zero in the window we reduce the value of k.
        # Since k is the maximum zeros allowed in a window.
            k -= 1 - nums[right]
        # A negative k denotes we have consumed all allowed flips and window has
        # more than allowed zeros, thus increment left pointer by 1 to keep the window size same.
            if k < 0:
        # If the left element to be thrown out is zero we increase k.
                k += 1 - nums[left]
                left += 1
        return right - left + 1