from typing import List

from pytest import mark

class Solution:
    def subsetsWithDup(nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()#To handle duplicate first we sort the array ( adjacent elements will be similar )
        def backtrack(nums,index=0,arr=[]):
            result.append( arr.copy() )
            for i in range( index, len(nums)):
                if i != index and nums[i] == nums[i-1]: #skip the duplicates, except for the first time
                    continue
                arr.append(nums[i]) #include the element
                backtrack(nums,i+1,arr ) #explore
                arr.pop() #remove the element
            
        backtrack(nums)
        return result


    def subsetsWithDup_recurse(self, nums: List[int]) -> List[List[int]]:
        nums.sort();
        starts = [0 for x in nums]
        result = [[]]
        for i in range(len(nums)):
            size = len(result)
            starts[i] = size
            j = 0;
            if i > 0 and nums[i-1] == nums[i]:
                j = starts[i-1]
            while j < size:
                result.append([] + result[j] + [nums[i]])
                j += 1
        return result
