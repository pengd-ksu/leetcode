class Solution:
    def calculate(self, s: str) -> int:
        # Will handle div and mul first, then store the number as positive or
        # negative, depending on previous operator. Sum will get the results.
        stack = []
        num = 0
        preop = '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = 10 * num + int(s[i])
            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s) - 1:
                if preop == '+':
                    stack.append(num)
                elif preop == '-':
                    stack.append(-num)
                elif preop == '*':
                    stack.append(stack.pop() * num)
                elif preop == '/':
                    # -3//2 == -2 in python3
                    tmp = stack.pop()
                    if tmp // num < 0 and tmp % num != 0:
                        stack.append(tmp // num + 1)
                    elif tmp // num < 0:
                        stack.append(tmp // num)
                    else:
                        stack.append(tmp // num)
                preop = s[i]
                num = 0
        return sum(stack)

class Solution:
    def calculate(self, s: str) -> int:
        # Key idea: loop over and hand multiplication and vision in the first place, because they have precedence.
        # Add '+' to the end of s to handle the last number
        num = 0
        pre_op = '+'
        stack = []
        s += '+'
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == ' ':
                continue
            else:
                if pre_op == '+':
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                elif pre_op == '*':
                    operand = stack.pop()
                    stack.append(num * operand)
                elif pre_op == '/':
                    operand = stack.pop()
                    stack.append(math.trunc(operand / num))
                num = 0
                pre_op = c
        return sum(stack)

class Solution:
    def calculate(self, s: str) -> int:
        # Very near time limit. First handle all mul and div, then 
        # plus and minus
        stack = []
        idx = 0
        while idx < len(s):
            if s[idx] == '+' or s[idx] == '-':
                stack.append(s[idx])
                idx += 1
            elif s[idx] == '*' or s[idx] == '/':
                op = s[idx]
                idx += 1
                while s[idx] == ' ':
                    idx += 1
                n = 0
                while idx < len(s) and s[idx].isdigit():
                    n = n * 10 + int(s[idx])
                    idx += 1
                pren = int(stack.pop())
                if op == '*':
                    result = pren * n
                else:
                    result = pren // n
                stack.append(str(result))# For later convenience
            elif s[idx].isdigit():
                n = 0
                while idx< len(s) and s[idx].isdigit():
                    n = n * 10 + int(s[idx])
                    idx += 1
                stack.append(str(n))
            else:#When s[idx] is blank space
                idx += 1
        if len(stack) == 1:
            return stack.pop()
        result = 0
        while stack:
            x = stack.pop(0) # pop out index 0
            if x.isdigit():
                result += int(x)
            elif x == '-':
                result -= int(stack.pop(0))
            elif x == '+':
                result += int(stack.pop(0))
        return result