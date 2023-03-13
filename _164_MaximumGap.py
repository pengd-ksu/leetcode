from typing import List
import functools

class Solution:
    def maximumGap(nums: List[int]) -> int:
        def radixSort(nums: List[int]) -> int:
            digitNums = len(str(max(nums)))
            for i in range(digitNums):
                bucket = [[] for _ in range(10)]
                for n in nums:
                    compareBit = (n // (10 ** i)) % 10
                    bucket[compareBit].append(n)
                nums = functools.reduce(lambda x, y: x + y, bucket)
            return nums
        if len(nums) == 1:
            return 0
        nums = radixSort(nums)
        gap = float('-inf')
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > gap:
                gap = nums[i] - nums[i - 1]
        return gap
"""
The first example is a demonstration of Radix Sort. The second is more concise
# Python program for implementation of Radix Sort
# A function to do counting sort of arr[] according to
# the digit represented by exp.
    def countingSort(arr, exp1):
        n = len(arr)
        # The output array elements that will have sorted arr
        output = [0] * (n)
        # initialize count array as 0
        count = [0] * (10)
        # Store count of occurrences in count[]
        for i in range(0, n):
            index = arr[i] // exp1
            count[index % 10] += 1
     
        # Change count[i] so that count[i] now contains actual
        # position of this digit in output array
        for i in range(1, 10):
            count[i] += count[i - 1]
     
        # Build the output array
        i = n - 1
        while i >= 0:
            index = arr[i] // exp1
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1
     
        # Copying the output array to arr[],
        # so that arr now contains sorted numbers
        i = 0
        for i in range(0, len(arr)):
            arr[i] = output[i]
     
    # Method to do Radix Sort
    def radixSort(arr):
     
        # Find the maximum number to know number of digits
        max1 = max(arr)
     
        # Do counting sort for every digit. Note that instead
        # of passing digit number, exp is passed. exp is 10^i
        # where i is current digit number
        exp = 1
        while max1 / exp > 0:
            countingSort(arr, exp)
            exp *= 10

    def radix_sort(nums):
        num_digits = len(str(max(nums)))
        A = nums 
        for i in range(num_digits):
            B = [[] for _ in range(10)]
            for num in A:
                bucket = (num // (10 ** i)) % 10
                B[bucket].append(num)
            #print(f'B: {B}')
            A = functools.reduce(lambda x, y: x+y, B)#Combine every sublist in B
            #print(f'A: {A}')
            
        return A
"""