from typing import List

from pytest import mark

class Solution:
    def sortColors(nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        #Dutch national flag, red->white->blue in order
        r, w, b = 0, 0, 0
        while r + w + b < n:
            k = n - 1 - b - w
            if nums[k] == 0:
                nums[k], nums[r] = nums[r], nums[k]
                r += 1
            elif nums[k] == 2:
                nums[k], nums[n-1-b] = nums[n-1-b], nums[k]
                b += 1
            else:
                w += 1
        return nums

    def sortColors_2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, len(nums) - 1
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1

@mark.parametrize('nums, expected', [
        ([2,0,2,1,1,0], [0,0,1,1,2,2]),
        ([2,0,1], [0,1,2]),
        ([0], [0]),
        ([1], [1]),
    ])

def test_sortColors(nums, expected):
    ans = Solution.sortColors(nums)
    assert ans == expected