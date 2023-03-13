import abc 
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass
    
class TreeNode(Node):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def evaluate(self):
        if self.val.isdigit():
            return int(self.val)
        elif self.val == "+":
            return self.left.evaluate() + self.right.evaluate()
        elif self.val == "-":
            return self.left.evaluate() - self.right.evaluate()
        elif self.val == "*":
            return self.left.evaluate() * self.right.evaluate()
        elif self.val == "/":
            return self.left.evaluate() // self.right.evaluate()


"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        cur = None
        stack = []
        for c in postfix:
            if c.isdigit():
                cur = TreeNode(c)
                stack.append(cur)
            else:
                cur = TreeNode(c)
                _right = stack.pop()
                _left = stack.pop()
                cur.left = _left
                cur.right = _right
                stack.append(cur)
        return cur
        
        
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""


import abc 
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass
    
class TreeNode(Node):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def evaluate(self):
        if self.val.isdigit():
            return int(self.val)
        elif self.val == "+":
            return self.left.evaluate() + self.right.evaluate()
        elif self.val == "-":
            return self.left.evaluate() - self.right.evaluate()
        elif self.val == "*":
            return self.left.evaluate() * self.right.evaluate()
        elif self.val == "/":
            return self.left.evaluate() // self.right.evaluate()


"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        cur = None
        stack = []
        for c in postfix:
            cur = TreeNode(c)
            if not c.isdigit():
                cur.right = stack.pop()
                cur.left = stack.pop()
            stack.append(cur)
        return cur

        
        
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
