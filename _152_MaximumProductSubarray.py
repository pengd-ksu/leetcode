from typing import List

class Solution:
    def maxProduct(nums: List[int]) -> int:
        #Need to keep track of both continuous max value and continuous min value so far, because the product including even number of negatives is still positive
        result, maxVal, minVal = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            tmpMax = nums[i] * maxVal
            tmpMin = nums[i] * minVal
            maxVal = max(nums[i], tmpMax, tmpMin)
            minVal = min(nums[i], tmpMax, tmpMin)
            result = max(result, maxVal)
            print(f'nums[{i}]: {nums[i]}, maxVal: {maxVal}, minVal: {minVal}, result: {result}')
        return result