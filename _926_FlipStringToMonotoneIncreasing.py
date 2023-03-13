class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # 1. Flip all the 1s so far to 0s; 2. flip the current zero to 1
        meet1 = 0
        flip = 0
        for c in s:
            if c == '1':
                meet1 += 1
            else:
                flip = min(meet1, flip+1)
                
        return flip