class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            else:
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(c)
        return len(stack)

    def minAddToMakeValid(self, s: str) -> int:
        """
        Keep track of the current balance of the string: the number of '(''s minus the number of ')''s.
        """
        ans = bal = 0
        for c in s:
            bal += 1 if c == '(' else -1
            if bal == -1:# To get it back into balance with '('
                ans += 1
                bal += 1
        return ans + bal # It could aslo be that s has more '('