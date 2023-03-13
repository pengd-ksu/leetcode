class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        elif n > 1:
            n, r = divmod(n, 2)
            if r != 0:
                return False
            else:
                return self.isPowerOfTwo(n)