"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # DFS
        if not node:
            return node
        seen = {}
        self.cloneGraph_recur(node, seen)
        return seen[node]
    
    def cloneGraph_recur(self, node: 'Node', seen: Dict['Node', 'Node']) -> 'Node':
        seen[node] = Node(node.val)
        for child in node.neighbors:
            if child in seen.keys():#original reference used as key
                seen[node].neighbors.append(seen[child])
            else:
                newchild = self.cloneGraph_recur(child, seen)
                seen[node].neighbors.append(newchild)
        return seen[node]#need to return for newchild during recursion