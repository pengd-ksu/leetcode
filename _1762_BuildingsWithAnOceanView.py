from typing import List

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ans = [len(heights) - 1]
        maxh = heights[-1]
        for i in range(len(heights) - 2, -1, -1):
            if maxh < heights[i]:
                maxh = heights[i]
                ans.append(i)
        ans.reverse()
        return ans

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # Iterate from left to right. Pop all the previous heights which 
        # are smaller than the current one.
        stack = []
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] <= h:
                stack.pop()
            stack.append(i)
        return stack

# A variant of findBuildings, when sea are on both sides
def bothViews(heights: List[int]) -> None:
    rmax, lmax = 0, 0
    ridx, lidx = 0, 0
    for i in range(len(heights)):
        if heights[i] > lmax:
            lidx = i
            lmax = heights[i]

    for j in range(len(heights) - 1, -1, -1):
        if heights[j] > rmax:
            ridx = j
            rmax = heights[j]

    lstack = []
    for i in range(lidx, -1, -1):
        while lstack and heights[lstack[-1]] <= heights[i]:
            lstack.pop()
        lstack.append(i)
    lstack.reverse()

    rstack = []
    for j in range(ridx, len(heights)):
        while rstack and heights[rstack[-1]] <= heights[j]:
            rstack.pop()
        rstack.append(j)
    print(f'rstack: {rstack},lstack: {lstack}')

heights = [1,3,2,2,4,4,5,5,5,3,4,2,3,1]
bothViews(heights)