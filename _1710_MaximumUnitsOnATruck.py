class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse = True)
        idx = 0
        ans = 0
        while idx < len(boxTypes) and truckSize:
            load = min(boxTypes[idx][0], truckSize)
            ans += load * boxTypes[idx][1]
            truckSize -= load
            idx += 1
        return ans

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = heapq.nlargest(len(boxTypes), boxTypes, key=lambda x: x[1])
        idx = 0
        ans = 0
        while idx < len(boxTypes) and truckSize:
            load = min(boxTypes[idx][0], truckSize)
            ans += load * boxTypes[idx][1]
            truckSize -= load
            idx += 1
        return ans