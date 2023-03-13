class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = random.choice(nums)
        left = [l for l in nums if l < pivot]
        right = [r for r in nums if r > pivot]
        equal = [e for e in nums if e == pivot]
        if k <= len(right):
            return self.findKthLargest(right, k)
        elif (k - len(right)) <= len(equal):
            return equal[0]
        else:
            return self.findKthLargest(left, k - len(right) - len(equal))

class Solution:
    def findKthLargest_1(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

    def findKthLargest_2(self, nums: List[int], k: int) -> int:
        nums.sort(reverse = True)
        return nums[k-1]

    def findKthLargest_3(self, nums: List[int], k: int) -> int:
        #Time Limit Exceeded, n square
        def insertionSort(arr):#From large to small
            if len(arr) == 1:
                return
            for j in range(1, len(arr)):
                tmp = arr[j]
                i = j - 1
                while i >= 0 and arr[i] < tmp:
                    arr[i+1] = arr[i]
                    i -= 1
                arr[i+1] = tmp
        insertionSort(nums)
        return nums[k-1]

    def findKthLargest_4(self, nums: List[int], k: int) -> int:
        def mergeSort(arr):#From large to small
            if len(arr) > 1:
                mid = len(arr) // 2
                left = arr[:mid]
                right = arr[mid:]
                mergeSort(left)
                mergeSort(right)
                i = j = k = 0
                while i < len(left) and j < len(right):
                    if left[i] >= right[j]:#equal to make sort stable
                        arr[k] = left[i]
                        i += 1
                    else:
                        arr[k] = right[j]
                        j += 1
                    k += 1
                while i < len(left):
                    arr[k] = left[i]
                    k += 1
                    i += 1
                while j < len(right):
                    arr[k] = right[j]
                    k += 1
                    j += 1
        mergeSort(nums)
        return nums[k-1]

    def findKthLargest_5(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            # 1. move pivot to end
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]  
            
            # 2. move all smaller elements to the left
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            nums[right], nums[store_index] = nums[store_index], nums[right]  
            
            return store_index
        
        def select(left, right, k_smallest):
            """
            Returns the k-th smallest element of list within left..right
            """
            if left == right:       # If the list contains only one element,
                return nums[left]   # return that element
            
            # select a random pivot_index between 
            pivot_index = random.randint(left, right)     
                            
            # find the pivot position in a sorted list   
            pivot_index = partition(left, right, pivot_index)
            
            # the pivot is in its final sorted position
            if k_smallest == pivot_index:
                 return nums[k_smallest]
            # go left
            elif k_smallest < pivot_index:
                return select(left, pivot_index - 1, k_smallest)
            # go right
            else:
                return select(pivot_index + 1, right, k_smallest)

        # kth largest is (n - k)th smallest 
        return select(0, len(nums) - 1, len(nums) - k)