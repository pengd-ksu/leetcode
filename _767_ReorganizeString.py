class Solution:
    def reorganizeString(self, s: str) -> str:
        # Use heap to maintain the pair of character and frequency, with
        # negative frequency so that the most frequenciest words will be
        # on top of the heap (now the smallest). Generate a new string
        # with alternating most frequenciest characters. Fetch two at a time,
        # because we need to push every character back (with lower frequency),
        # it is possible we fetch a same character next time. If the heap 
        # is odd number, and final one appear more than once, it will 
        # inevitably end in repeated adjacent characters.
        # heapq is min heap in python
        import collections
        cnt = collections.Counter(s)
        h = [(-v, k) for k, v in cnt.items()]
        import heapq
        heapq.heapify(h)
        ans = ''
        while len(h) > 1:
            x = heapq.heappop(h) # Suppose s='aaaab', fetch 'a' and pushed it
            # back, we would fetch 'a' again next time.
            y = heapq.heappop(h)
            ans += x[1]
            ans += y[1]
            if x[0] < -1:
                heapq.heappush(h, (x[0]+1, x[1]))
            if y[0] < -1:
                heapq.heappush(h, (y[0]+1, y[1]))
        if h:
            if h[0][0] < -1:
                return ''
            else:
                ans += h[0][1]
        return ans