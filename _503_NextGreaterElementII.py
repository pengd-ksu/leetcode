class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        ans = [-1] * len(nums)
        for i, n in enumerate(nums):
            while stack and nums[stack[-1]] < n:
                ans[stack.pop()] = n
            stack.append(i)
        # Now the stack is monotonic decreasing, every element is larger than 
        # all the elements to its right. Let's check its left side
        for i, n in enumerate(nums):
            while stack and nums[stack[-1]] < n:
                ans[stack.pop()] = n
        return ans