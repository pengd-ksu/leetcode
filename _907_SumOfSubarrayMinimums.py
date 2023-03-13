"""
This forms the basis of the solution: we build monotonously incressing (well, 
strictly speaking - non-decreasing) stack. And then find previous less or 
equal value and reuse it's sum:

(trick: we add zeros to arr and stack to avoid dealing with empty stack)
"""
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr = [0] + arr
        result = [0]*len(arr)
        stack = [0]
        for i in range(len(arr)):
            while arr[stack[-1]] > arr[i]:
                stack.pop()
            j = stack[-1]
            result[i] = result[j] + (i-j)*arr[i]
            stack.append(i)
        return sum(result) % (10**9+7)