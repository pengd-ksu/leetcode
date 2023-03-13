from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        # O(1) time 
        #if k == len(nums):
        #    return nums
        
        # 1. build hash map : character and how often it appears
        # O(N) time
        count = Counter(nums)   
        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return heapq.nlargest(k, count.keys(), key=count.get)

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        unique = list(count.keys())
        
        def partition(left, right, pivot_index) -> int:
            pivot_frequency = count[unique[pivot_index]]
            # 1. move pivot to end
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]  
            
            # 2. move all less frequent elements to the left
            store_index = left
            for i in range(left, right):
                if count[unique[i]] < pivot_frequency:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            unique[right], unique[store_index] = unique[store_index], unique[right]  
            
            return store_index
        
        def quickselect(left, right, k_smallest) -> None:
            """
            Sort a list within left..right till kth less frequent element
            takes its place. 
            """
            # base case: the list contains only one element
            if left == right: 
                return
            
            # select a random pivot_index
            pivot_index = random.randint(left, right)     
                            
            # find the pivot position in a sorted list   
            pivot_index = partition(left, right, pivot_index)
            
            # if the pivot is in its final sorted position
            if k_smallest == pivot_index:
                 return 
            # go left
            elif k_smallest < pivot_index:
                quickselect(left, pivot_index - 1, k_smallest)
            # go right
            else:
                quickselect(pivot_index + 1, right, k_smallest)
         
        n = len(unique) 
        # kth top frequent element is (n - k)th less frequent.
        # Do a partial sort: from less frequent to the most frequent, till
        # (n - k)th less frequent element takes its place (n - k) in a sorted array. 
        # All element on the left are less frequent.
        # All the elements on the right are more frequent.  
        quickselect(0, n - 1, n - k)
        # Return top k frequent elements
        return unique[n - k:]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        # Frequency could range from zero to len(nums), 1 + len(nums)
        counter = collections.Counter(nums)
        for n, freq in counter.items():
            bucket[freq].append(n)
        flat_list = [ele for sublist in bucket for ele in sublist]
        return flat_list[::-1][:k]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def myChain(*iterables):
            for it in iterables:
                for element in it:
                    yield element
        counter = collections.Counter(nums)
        # One more because suppose there's only element in nums, and its 
        # frequnce will be 1. Then bucket[1] will be out of index range
        bucket = [[] for _ in range(len(nums) + 1)]
        for n, freq in counter.items():
            bucket[freq].append(n)
        flatList = list(myChain(*bucket))
        #flatList = list(itertools.chain(*bucket))
        return flatList[::-1][:k]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(list)
        counter = collections.Counter(nums)
        for n, cnt in counter.items():
            freq[cnt].append(n)#In order of large to small
        
        ans = []
        for times in reversed(range(len(nums) + 1)):
            ans.extend(freq[times])
            #if times not in freq, freq[times] will return list, and extend 
            # will add nothing in the list of ans
            if len(ans) == k:
                return ans