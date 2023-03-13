"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:#Key: root.parent = None
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        parent = {}
        while p:
            parent[p] = p.parent
            if q in parent:
                return q
            p = p.parent
        while q:
            if q in parent:
                return q
            parent[q] = q.parent
            q = q.parent

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def getDepth(node):
            depth = 0
            while node:
                depth += 1
                node = node.parent
            return depth
        pDepth = getDepth(p)
        qDepth = getDepth(q)
        
        # Only one of the two for loops will be executed, depending which is bigger
        for _ in range(pDepth - qDepth):
            p = p.parent
        for _ in range(qDepth - pDepth):
            q = q.parent
        while p != q:
            p = p.parent
            q = q.parent
        return p