from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Time Limit Exceeded. Time complexity: n^2
        left = 0
        count = 0
        while left < len(nums):
            if nums[left] == k:
                count += 1
            if left == len(nums) - 1:   #seems unnecessary?
                break                   #seems unnecessary?
            end = left + 1
            while end < len(nums):
                if sum(nums[left: end + 1]) == k:
                    count += 1
                end += 1
            left += 1
        return count

    def subarraySum_2(nums: List[int], k: int) -> int:
        # Instead of getting a sum equals to k, we are searching for a increase 
        # sum euqls to k from an accumulated array. Double loop for subtraction 
        # between accumulations could get results, but will end in square 
        # costs. The key information is how may from the past could we get an 
        # accumulation that equals to sums(so far) - k. Store it in a 
        # dictionary will avoid duplicate calculations.
        # d = {0: 1}
        # A trick is to add 0 as just once in the beginning, to perform the 
        # first sums of k.
        count = 0
        sums = 0
        d = {0: 1} # Handle the case when a single element is equal to k
        for n in nums:
            sums += n
            count += d.get(sums-k, 0)#So far, how many would be counted up to k
            d[sums] = d.get(sums, 0) + 1
        return count


n = [1,1,1,-2,1,1]
print(Solution.subarraySum_2(n, 2))