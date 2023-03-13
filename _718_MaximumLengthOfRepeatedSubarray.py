class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0 for _ in range(len(nums2) + 1)] for _ in range(len(nums1) + 1)]
        #0 row and 0 col contain 0s as dummy variables for convenience of calculation
        longest = 0
        for i in range(1, len(nums1) + 1):
            for j in range(1, len(nums2) + 1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = 0
                longest = max(longest, dp[i][j])
        return longest

    def findLength_2(self, nums1: List[int], nums2: List[int]) -> int:
        nums2Str = ''.join([chr(n) for n in nums2])
        longest = 0
        maxStr = ''
        #Once it met the longest seq, maxStr will keep the length and continue checking the rest.
        for n in nums1:
            maxStr += chr(n)
            if maxStr in nums2Str:
                longest = max(longest, len(maxStr))
            else:
                maxStr = maxStr[1:]
        return longest