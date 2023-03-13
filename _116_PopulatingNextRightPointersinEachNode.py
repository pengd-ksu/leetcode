"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        #every node already sets next to None as default 
        if root:
            if root.left and root.right:
                root.left.next = root.right
                if root.next:
                    root.right.next = root.next.left
            self.connect(root.left)
            self.connect(root.right)
        return root

    def connect_level(self, root: 'Node') -> 'Node':
        if not root:
            return root
        level = [root]
        while level:
            nextLevel = []
            for i in range(len(level)):
                if i < len(level) - 1:
                    level[i].next = level[i + 1]
            #check left and right individually in case not perfect bst
                if level[i].left:
                    nextLevel.append(level[i].left)
                if level[i].right:
                    nextLevel.append(level[i].right)
            level = nextLevel
        return root