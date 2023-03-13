class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            stack_length = len(stack)
            if stack_length == 0 or s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            elif s[i] == ')' and stack[stack_length - 1] == '(':
                stack.pop(stack_length - 1)
            elif s[i] == ']' and stack[stack_length - 1] == '[':
                stack.pop(stack_length - 1)
            elif s[i] == '}' and stack[stack_length - 1] == '{':
                stack.pop(stack_length - 1)
            else:
                return False
        return len(stack) == 0

    def isValid_2(self, s: str) -> bool:
        stack = []
        for l in s:
            if l == '(' or l == '[' or l == '{':
                stack.append(l)
            elif l == ')':
                if stack:
                    last = stack.pop()
                    if last != '(':
                        return False
                else:
                    return False
            elif l == ']':
                if stack:
                    last = stack.pop()
                    if last != '[':
                        return False
                else:
                    return False
            elif l == '}':
                if stack:
                    last = stack.pop()
                    if last != '{':
                        return False
                else:
                    return False
        if not stack:
            return True

    def isValid_3(self, s: str) -> bool:
        stack = []
        dic = {'(': ')', '[': ']', '{': '}'}
        for l in s:
            if l in dic.keys():
                stack.append(l)
            elif len(stack) == 0 or l != dic[stack.pop()]:
                return False
        return len(stack) == 0