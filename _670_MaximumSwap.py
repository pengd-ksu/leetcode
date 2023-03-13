class Solution:
    def maximumSwap(self, num: int) -> int:
        # Key: find the largest single number from the right; check if there's
        # a chance that any number on the left side of the largest one can be 
        # swapped.
        num_str = list(str(num))
        max_str, max_idx = -1, -1
        left, right = -1, -1
        
        for i in range(len(num_str) - 1, -1, -1):
            if int(num_str[i]) > int(max_str):
                max_str = num_str[i]
                max_idx = i
            if int(num_str[i]) < int(max_str):
                left = i
                right = max_idx
        if left == -1:
            return num
        else:
            num_str[left], num_str[right] = num_str[right], num_str[left]
            return int(''.join(num_str))

class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        max_str, max_idx = -1, -1
        left, right = -1, -1
        
        for i in range(len(num_str) - 1, -1, -1):
            if int(num_str[i]) > int(max_str):
                max_str = num_str[i]
                max_idx = i
                
            elif int(num_str[i]) < int(max_str):
                left = i
                right = max_idx
                
        if left == -1:
            return num
        else:
            num_str[left], num_str[right] = num_str[right], num_str[left]
            return int(''.join(num_str))