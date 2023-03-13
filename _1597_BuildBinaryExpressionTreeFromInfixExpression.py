# Mar 12, 2022. Too hard for me. Come back after CS61A.

# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def expTree(self, s: str) -> 'Node':
        def build(op, right, left):
            return Node(op, left, right)
        
        def compare(op1, op2):
            if op1 == '(' or op1 == ')': return False
            return op1 in {'*','/' } or op2 in {'+','-' }
        
        node_s, op_s = [], []
        
        for c in s:
            if c.isdigit(): node_s.append(Node(c))
            elif c == '(': op_s.append(c)
            elif c == ')':
                while op_s[-1] != '(':
                    node_s.append(build(op_s.pop(), node_s.pop(), node_s.pop()))
                op_s.pop() # remove '('
            else:
                while op_s and compare(op_s[-1], c):
                    node_s.append(build(op_s.pop(), node_s.pop(), node_s.pop()))
                op_s.append(c)
                
        while op_s:
            node_s.append(build(op_s.pop(), node_s.pop(), node_s.pop()))
        
        return node_s[-1]


# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Standard parser implementation based on this BNF
    #   s := expression
    #   expression := term | term { [+,-] term] }
    #   term := factor | factor { [*,/] factor] }
    #   factor :== digit | '(' expression ')'
    #   digit := [0..9]
    
    def expTree(self, s: str) -> 'Node':
        tokens = collections.deque(list(s))
        return self.parse_expression(tokens)

    def parse_expression(self, tokens):
        lhs = self.parse_term(tokens)
        while len(tokens) > 0 and tokens[0] in ['+', '-']:
            op = tokens.popleft()
            rhs = self.parse_term(tokens)
            lhs = Node(val=op, left=lhs, right=rhs)
        return lhs
    
    def parse_term(self, tokens):
        lhs = self.parse_factor(tokens)
        while len(tokens) > 0 and tokens[0] in ['*', '/']:
            op = tokens.popleft()
            rhs = self.parse_factor(tokens)
            lhs = Node(val=op, left=lhs, right=rhs)
        return lhs

    def parse_factor(self, tokens):
        if tokens[0] == '(':
            tokens.popleft() # consume '('
            node = self.parse_expression(tokens)
            tokens.popleft() # consume ')'
            return node
        else:
            # Single operand
            token = tokens.popleft()
            return Node(val=token)



pr = {'*': 1, '/': 1, '+': 2, '-': 2, ')': 3, '(': 4}

class Solution(object):
    def apply(self, numSt, opSt):
        right = numSt.pop()
        left = numSt.pop()
        return Node(opSt.pop(), left, right)
    def expTree(self, s):
        numSt, opSt = [], []
        i = 0
        while (i < len(s)):
            c = s[i]
            i += 1
            if c.isnumeric(): numSt.append(Node(c))
            else:                
                if c in '(': opSt.append('(')
                else:
                    while(len(opSt) > 0 and pr[c] >= pr[opSt[-1]]):
                        numSt.append(self.apply(numSt, opSt))
                    if (c == ')'): opSt.pop()
                    else: opSt.append(c)
        while(len(opSt) > 0): numSt.append(self.apply(numSt, opSt))
        return numSt.pop()