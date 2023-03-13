class Solution:
    def decodeString(self, s: str) -> str:
        curNum = 0
        curStr = ''
        stack = []
        for c in s:
            if c.isdigit():
                curNum = curNum * 10 + int(c)
            elif c == '[':
                stack.append(curNum)
                stack.append(curStr)
                curStr = ''
                curNum = 0
            elif c == ']':
                prevStr = stack.pop()
                repeat = stack.pop()
                curStr = prevStr + repeat * curStr
            else:
                curStr += c
        return curStr