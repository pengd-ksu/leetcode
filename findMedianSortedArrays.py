class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = []
        while(nums1 and nums2):
            for i1, num1 in enumerate(nums1):
                for i2, num2 in enumerate(nums2):
                    if num1 < num2:
                        if num1 not in nums:
                            nums.append(nums1.pop(i1))
                    else:
                        if num2 not in nums:
                            nums.append(nums2.pop(i2))
        if nums1:
            nums.extend(nums1)
        else:
            nums.extend(nums2)
        if len(nums) % 2 == 0:
            return (nums[len(nums)/2-1]+nums[len(nums)/2])/2.0
        else:
            return nums[(len(nums)-1)/2]