class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        cur = 0
        while left <= right:
            h = min(height[left], height[right])
            cur = max(cur, h * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return cur