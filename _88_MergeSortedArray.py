from typing import List
from pytest import mark

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        while p1 >= 0 or p2 >= 0:
            if p2 < 0:
                nums1[p] = nums1[p1]
                p -= 1
                p1 -= 1
            elif p1 < 0:
                nums1[p] = nums2[p2]
                p -= 1
                p2 -= 1
            else:
                if nums1[p1] > nums2[p2]:
                    nums1[p] = nums1[p1]
                    p -= 1
                    p1 -= 1
                else:
                    nums1[p] = nums2[p2]
                    p -= 1
                    p2 -= 1


#It's different from the version on leetcode, because we need to return nums1
class Solution:
    def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m >= 0 and n >= 0:
            if m == 0:
                for j in range(n):
                    nums1[j] = nums2[j]
                return nums1
            if n == 0:
                return nums1
            elif nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        return nums1

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1
        p2 = n - 1
        for p in range(m+n-1, -1, -1):
            if p2 < 0:#clever
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1

@mark.parametrize('nums1, m, nums2, n, expected', [
        ([1,2,3,0,0,0], 3, [2,5,6], 3, [1,2,2,3,5,6]),
        ([1], 1, [], 0, [1]),
        ([0], 0, [1], 1, [1]),
    ])

def test_merge(nums1, m, nums2, n, expected):
    ans = Solution.merge(nums1, m, nums2, n)
    assert ans == expected