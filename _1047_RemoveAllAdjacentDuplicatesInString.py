class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:# stack empty, or stack[-1] != c
                stack.append(c)
        return ''.join(stack)

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            while stack and stack[-1] == c:
                stack.pop()
                break
            else:
                stack.append(c)
        return ''.join(stack)