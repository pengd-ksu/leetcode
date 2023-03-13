class MedianFinder: # Two heaps, logn
    def __init__(self):
        self.lo = []
        self.hi = []
        
    def addNum(self, num):
        # A max-heap to store the smaller half of the input numbers and a min-heap to store the larger half of the input numbers
        # lo is maxheap, and hi is minheap
        heappush(self.lo, -num)
        heappush(self.hi, -self.lo[0])
        heappop(self.lo)
        
        if len(self.lo) < len(self.hi):
            heappush(self.lo, -self.hi[0])
            heappop(self.hi)
            
    def findMedian(self):
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        else:
            return (self.hi[0] - self.lo[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

class MedianFinder: # Sort when fetch median
    def __init__(self):
        self.ls = []

    def addNum(self, num: int) -> None:
        self.ls.append(num)
        
    def findMedian(self) -> float:
        self.ls.sort()
        n = len(self.ls)
        if n % 2 == 1:
            return self.ls[n // 2]
        return (self.ls[n // 2 - 1] + self.ls[n // 2]) / 2


class MedianFinder: 
# Suppose list is already sorted, binary search to insert new number
# Both bisect and insert can handle empty list
    def __init__(self):
        self.ls = []

    def addNum(self, num: int) -> None:
        # Both bisect and insert can handle empty list
        import bisect
        pos = bisect.bisect_left(self.ls, num)
        self.ls.insert(pos, num)
        
    def findMedian(self) -> float:
        n = len(self.ls)
        if n % 2 == 1:
            return self.ls[n // 2]
        return (self.ls[n // 2 - 1] + self.ls[n // 2]) / 2