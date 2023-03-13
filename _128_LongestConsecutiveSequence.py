class Solution:
    def longestConsecutive_hash(self, nums: List[int]) -> int:
        hashset = {n: True for n in nums}
        ans = 0
        for n in nums:
            if hashset[n]:
                hashset[n] = False
                cur = 1
                up, down = n + 1, n - 1
                while up in hashset:
                    hashset[up] = False
                    cur += 1
                    up += 1
                while down in hashset:
                    hashset[down] = False
                    cur += 1
                    down -= 1
                ans = max(ans, cur)
        return ans

    def longestConsecutive_sort(nums: List[int]) -> int:
        # This is O(nlgn)
        if not nums:
            return 0
        nums.sort() # O(nlgn)
        maxSeq, curSeq = 1, 1
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:#0, 1, 1, 2 are counted as 3, skip the 
            #same one in a sequence and continue counting
                if nums[i] == nums[i + 1] - 1:
                    curSeq += 1
                else:
                    maxSeq = max(maxSeq, curSeq)
                    curSeq = 1
        return max(maxSeq, curSeq)

    def longestConsecutive_brute(nums: List[int]) -> int:
        maxSeq = 0
        for n in nums:
            curNum = n
            curSeq = 1
            while curNum + 1 in nums:
                curNum += 1
                curSeq += 1
            maxSeq = max(maxSeq, curSeq)
        return maxSeq

    def longestConsecutive(nums: List[int]) -> int:
        maxSeq = 0
        nums = set(nums)
        for n in nums:
            curNum = n
            curSeq = 1
            if curNum - 1 in nums: # To avoid redundant counting. Only
                #count from the smallest number.
                continue
            while curNum + 1 in nums:
                curNum += 1
                curSeq += 1
            maxSeq = max(maxSeq, curSeq)
        return maxSeq