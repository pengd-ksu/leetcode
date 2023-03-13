class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Need a data structure that pops out previous higher heights and calculate
        # corresponding areas. Two tricks: append 0 to the end of height so that
        # it would pop out all the heights, because 0 is lower than any height. But also,
        # heights[stack[-1]] will always be 0, no new height could pop -1 from stack; 
        # Use -1 as the initial element in the stack, so that the lowest height will 
        # cover whole areas. Think about this: width=i-stack[-1]-1. The last one in stack
        # is -1, it will take over the whole width for the lowest height
        stack = [-1]
        heights.append(0)
        area = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                idx = stack.pop()
                area = max(area, heights[idx]*(i-stack[-1]-1))
            stack.append(i)
        return area