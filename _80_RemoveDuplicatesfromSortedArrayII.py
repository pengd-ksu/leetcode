class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return
        
        idx1, idx2, count = 1, 1, 1
        prev = nums[0]
        while idx1 <= n - 1 and idx2 <= n - 1:
            if nums[idx2] == prev:
                count += 1
                if count <= 2:
                    nums[idx1] = nums[idx2]
                    idx1 += 1                 
            else:
                nums[idx1] = nums[idx2]
                prev = nums[idx2]
                count = 1
                idx1 += 1
                
            idx2 += 1

        for i in range(idx1, n):
            nums[i] = '_'
        return idx1#Because it will check nums[:idx1+1]

    def removeDuplicates_2(self, nums: List[int]) -> int:
        # First change all duplicates (appearing more than twice) to '_'
        # Second iterate with two pointers as the technique in #283
        # Edge case: the function returns k. If there're duplicates, it will
        # check nums[:k]. Which means, if there are no duplicates, we should
        # return the whole nums.
        count = 1
        prev = nums[0]
        hasDuplicates = False
        for i in range(1, len(nums)):
            if nums[i] == prev:
                if count == 2:
                    nums[i] = '_'
                    hasDuplicates = True
                else:
                    count += 1
            else:
                prev = nums[i]
                count = 1
        duplicate = 0
        for j in range(len(nums)):
            if nums[j] != '_':
                nums[duplicate], nums[j] = nums[j], nums[duplicate]
                duplicate += 1

        return duplicate if hasDuplicates else len(nums)

    def removeDuplicates(self, nums: List[int]) -> int:
        # The nums is alreayd sorted in non-decreasing order, so initial j and i
        # are three consecutive sequences. If nums[j] == nums[i-1], it means in 
        # the beginning there are three same numbers. i is kept to track
        # duplicate numbers that appear at least three times.
        n = len(nums)
        if n < 3:
            return n
        i , j = 1, 2
        while j < n:
            if nums[i-1] != nums[j]:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i + 1