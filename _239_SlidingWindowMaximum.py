class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #A queue data structure that maintains largest element's index on the left
        #Once met with a new ele, will pop out from right(recently added) all
        #the elements that are smaller than the new one
        #Once out of window, will pop the largest element from the left, because
        #all the elements in the queue is maintained according to time line from
        #left to right
        #Once index could be large enough to from a window, add the largest element
        #each step (not pop)
        q = collections.deque()
        ans = []
        for idx, cur in enumerate(nums):
            while q and nums[q[-1]] < cur:
                q.pop()
            q.append(idx)
            if q[0] == idx - k:#largest element out of window
                q.popleft()
            if idx >= k - 1:
                ans.append(nums[q[0]])
        return ans