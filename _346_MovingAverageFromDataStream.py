class MovingAverage:

    def __init__(self, size: int):
        self.s = size
        self.q = collections.deque()
        self.total = 0
        self.num = 0

    def next(self, val: int) -> float:
        self.num += 1
        self.total += val
        self.q.append(val)
        
        if self.num > self.s:
            out = self.q.popleft()
            self.total -= out
            self.num -= 1
        
        return self.total / self.num

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

class MovingAverage:

    def __init__(self, size: int):
        self.s = size
        self.q = []

    def next(self, val: int) -> float:
        size, queue = self.s, self.q
        queue.append(val)
        window_sum = sum(queue[-size:])
        
        return window_sum / min(len(queue), size)

class MovingAverage:

    def __init__(self, size: int):
        import collections
        self.s = size
        self.q = collections.deque()
        self.window_sum = 0
        self.count = 0

    def next(self, val: int) -> float:
        self.count += 1
        self.q.append(val)
        tail = self.q.popleft() if self.count > self.s else 0
        #self.count will always be larger than self.count once exceeding, because we didn't update its values here.
        self.window_sum = self.window_sum - tail + val
        
        return self.window_sum / min(self.s, self.count)

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = [0] * self.size
        self.head = 0
        self.window_sum = 0
        # number of elements seen so far
        self.count = 0

    def next(self, val: int) -> float:
        self.count += 1
        # calculate the new sum by shifting the window
        tail = (self.head + 1) % self.size
        self.window_sum = self.window_sum - self.queue[tail] + val
        # move on to the next head
        self.head = (self.head + 1) % self.size
        self.queue[self.head] = val
        return self.window_sum / min(self.size, self.count)