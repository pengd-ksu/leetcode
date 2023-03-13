class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in '+-*/':
                b = stack.pop()
                a = stack.pop()
                if t == '+':
                    result = a + b
                elif t == '-':
                    result = a - b
                elif t == '*':
                    result = a * b
                elif t == '/':
                    result = int(a / b)#case 13 / 5, expecting 2
                stack.append(result)
            else:
                stack.append(int(t))
        return stack.pop()

    def evalRPN(self, tokens: List[str]) -> int:
        import operator
        OPERATORS = {
            '*': operator.mul,
            '/': operator.truediv,
            '+': operator.add,
            '-': operator.sub
        }

        stack = list()
        for button in tokens:
            if button.isdigit() or button[1:].isdigit():
                stack.append(int(button))#int() will keep the negative sign
            else:
                right_oper = stack.pop()
                left_oper = stack.pop()
                
                calculated_param = int(OPERATORS[button](left_oper, right_oper))  # Passing arguments
                
                stack.append(calculated_param)

        result = stack.pop()
        return result