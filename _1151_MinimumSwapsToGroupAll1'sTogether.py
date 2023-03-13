class Solution:
    def minSwaps(self, data: List[int]) -> int:
        # Key idea: get the total of 1s, set a sliding window with the same 
        # size, check which window has the least zeros.
        ones = sum(data)
        if ones == 0 or ones == 1:
            return 0
        left = 0
        right = ones - 1
        swap = float('inf')
        window = sum(data[left: right])
        while right < len(data):
            window += data[right]
            swap = min(swap, ones - window)
            window -= data[left]
            left += 1
            right += 1
        return swap

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = sum(data)
        cnt_one = max_one = 0
        queue = collections.deque()
        
        for i in range(len(data)):
            queue.append(data[i])
            cnt_one += data[i]
            
            if len(queue) > ones:
                cnt_one -= queue.popleft()
            max_one = max(max_one, cnt_one)
        return ones - max_one