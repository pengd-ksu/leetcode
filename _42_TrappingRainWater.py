class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        ans = 0
        nums = len(height)
        left_max, right_max = [0 for i in range(nums)], [0 for i in range(nums)]
        left_max[0] = height[0]
        for i in range(1, nums):
            left_max[i] = max(height[i], left_max[i-1])
        right_max[nums-1] = height[nums-1]
        for i in range(nums - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i+1])
        for i in range(1, nums-1):
            ans += min(left_max[i], right_max[i]) - height[i]
        return ans

    def trap_2(self, height: List[int]) -> int:
        waterlevel = []
        left = 0
        for h in height:
            left = max(left, h)
            waterlevel.append(left) # For every h, there will be a height in waterlevel
        right = 0
        for i, h in reversed(list(enumerate(height))):
            right = max(right, h)
            waterlevel[i] = min(right, waterlevel[i]) - h
        return sum(waterlevel)

    def trap_3(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0
        volume = 0
        left, right = 0, len(height) - 1
        l_max, r_max = height[left], height[right]
        while left < right:
            l_max, r_max = max(height[left], l_max), max(height[right], r_max)
            if l_max <= r_max:
                volume += l_max - height[left]
                left += 1
            else:
                volume += r_max - height[right]
                right -= 1
        return volume