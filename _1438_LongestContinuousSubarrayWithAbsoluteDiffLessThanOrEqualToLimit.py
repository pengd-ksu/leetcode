from typing import List
import heapq

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxheap = []
        minheap = []
        res = i = 0
        
        for j, n in enumerate(nums):
            heapq.heappush(maxheap, [-n, j])
            heapq.heappush(minheap, [n, j])
            # If exceeds limit, pop at least one of the least and largest
            # i is the smaller of the indices of least and largest plus one
            # j - i + 1 keeps record of the length of valid continuous array
            while -maxheap[0][0] - minheap[0][0] > limit:
                i = min(maxheap[0][1], minheap[0][1]) + 1
                while maxheap[0][1] < i: heapq.heappop(maxheap)
                while minheap[0][1] < i: heapq.heappop(minheap)
            res = max(res, j - i + 1)
        return res

class Solution:
    #sliding window and two monotonic queues to keep track of the window max 
    # and window min.
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_deque, max_deque = deque(), deque()
        l = r = 0
        ans = 0
        
        while r < len(nums):
            while min_deque and nums[min_deque[-1]] > nums[r]:
                min_deque.pop()
            while max_deque and nums[max_deque[-1]] < nums[r]:
                max_deque.pop()
            
            min_deque.append(r)
            max_deque.append(r)
            
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                l += 1
                if l > min_deque[0]:
                    min_deque.popleft()
                if l > max_deque[0]:
                    max_deque.popleft()
            
            ans = max(ans, r - l + 1)
            r += 1
            
        return ans