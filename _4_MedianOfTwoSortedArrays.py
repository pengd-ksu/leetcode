class Solution:
"""
The best solution I've seen so far! Those ones searching for k+1 element then 
compare the last 2 elements in each array (which originates from this article 
I believe) are way too complex and troublesome compare with this one. Thanks 
for sharing!
However, one thing need pay attention is, array slicing in python is O(n) 
complexity, so if one really pursues O(log(m+n)) complexity, he should pass 
start and end indexes instead, though the code may look a little verbose.
"""
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = len(nums1) + len(nums2)
        if l % 2 == 1:
            return self.kth(nums1, nums2, l // 2)
        else:
            return (self.kth(nums1, nums2, l // 2) + \
                self.kth(nums1, nums2, l // 2 - 1)) / 2
    
    def kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        ia, ib = len(a) // 2 , len(b) // 2
        ma, mb = a[ia], b[ib]
        # when k is bigger than the sum of a and b's median indices 
        if ia + ib < k:
        # if a's median is bigger than b's, b's first half doesn't include k
            if ma > mb:
                return self.kth(a, b[ib + 1:], k - ib - 1)
            else:
                return self.kth(a[ia + 1:], b, k - ia - 1)
        # when k is smaller than the sum of a and b's indices
        else:
        # if a's median is bigger than b's, a's second half doesn't include k
            if ma > mb:
                return self.kth(a[:ia], b, k)
            else:
                return self.kth(a, b[:ib], k)


class Solution:# This solution doesn't use slicing
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        # when total length is odd, the median is the middle
        if (len1 + len2) % 2 != 0:
            return self.get_kth(nums1, nums2, 0, len1-1, 0, len2-1, (len1+len2)//2)
        else:
        # when total length is even, the median is the average of the middle 2
            middle1 = self.get_kth(nums1, nums2, 0, len1-1, 0, len2-1, (len1+len2)//2)
            middle2 = self.get_kth(nums1, nums2, 0, len1-1, 0, len2-1, (len1+len2)//2-1)
            return (middle1 + middle2) / 2

    def get_kth(self, nums1, nums2, start1, end1, start2, end2, k):
        if start1 > end1:
            return nums2[k-start1]
        if start2 > end2:
            return nums1[k-start2]
        
        middle1 = (start1 + end1) // 2
        middle2 = (start2 + end2) // 2
        middle1_value = nums1[middle1]
        middle2_value = nums2[middle2]
        
        # if sum of two median's indicies is smaller than k
        if (middle1 + middle2) < k:
            # if nums1 median value bigger than nums2, then nums2's first half 
            # will always be positioned before nums1's median, so k would never 
            # be in num2's first half
            if middle1_value > middle2_value:
                return self.get_kth(nums1, nums2, start1, end1, middle2+1, end2, k)
            else:
                return self.get_kth(nums1, nums2, middle1+1, end1, start2, end2, k)
        # if sum of two median's indicies is bigger than k
        else:
            # if nums1 median value bigger than nums2, then nums2's first half 
            # would be merged before nums1's first half, thus k always come 
            # before nums1's median, then nums1's second half would never 
            # include k
            if middle1_value > middle2_value:
                return self.get_kth(nums1, nums2, start1, middle1-1, start2, end2, k)
            else:
                return self.get_kth(nums1, nums2, start1, end1, start2, middle2-1, k)


class Solution:# Wrong, time: O(n+m). Required log(n+m)
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        idx1 = idx2 = 0
        while nums1[idx1:] and nums2[idx2:]:
            if nums1[idx1] < nums2[idx2]:
                nums.append(nums1[idx1])
                idx1 += 1
            else:
                nums.append(nums2[idx2])
                idx2 += 1
        if idx1 <= len(nums1) - 1:
            nums.extend(nums1[idx1:])
        if idx2 <= len(nums2) - 1:
            nums.extend(nums2[idx2:])
        if len(nums) % 2 != 0:
            return nums[(len(nums)) // 2]
        else:
            return (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2

class Solution:# Also wrong, time: O(n+m). Required log(n+m)
    def findMedianSortedArrays_2(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        idx1 = idx2 = 0
        while idx1 < len(nums1) and idx2 < len(nums2):
            if nums1[idx1] <= nums2[idx2]:
                nums.append(nums1[idx1])
                idx1 += 1
            else:
                nums.append(nums2[idx2])
                idx2 += 1
        if idx1 < len(nums1):
            nums.extend(nums1[idx1:])
        if idx2 < len(nums2):
            nums.extend(nums2[idx2:])
        if len(nums) % 2 != 0:
            return nums[(len(nums)) // 2]
        else:
            return (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2