class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indexDict = {}
        for i in range(len(nums)):
            if nums[i] in indexDict.keys():
                if abs(indexDict[nums[i]] - i) <= k:
                    return True
                else:
                    indexDict[nums[i]] = i
            else: 
                indexDict[nums[i]] = i
        return False

    def containsNearbyDuplicate_slidingWindow(self, nums: List[int], k: int) -> bool:
        #Keep a sliding window of index range within k in a set
        slidingSet = set()
        for i in range(len(nums)):
            if i > k:
                slidingSet.remove(nums[i - 1 - k])
            if nums[i] in slidingSet:
                return True
            slidingSet.add(nums[i])
        return False