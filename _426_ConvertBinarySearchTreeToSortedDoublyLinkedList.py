"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution: # This solution is not in-place
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        
        ans = []

        def inorder(node):
            if node:
                inorder(node.left)
                ans.append(node)
                inorder(node.right)
            
        inorder(root)
        ans[0].left = ans[-1]
        ans[-1].right = ans[0]
        for i in range(len(ans) - 1):
            ans[i].right = ans[i + 1]
            ans[i + 1].left = ans[i]
        return ans[0]

class Solution: # This solution is not in-place neither
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        
        def inorder(node):
            return inorder(node.left) + [node] + inorder(node.right) if node else []
            
        ans = inorder(root)
        ans[0].left = ans[-1]
        ans[-1].right = ans[0]
        for i in range(len(ans) - 1):
            ans[i].right = ans[i + 1]
            ans[i + 1].left = ans[i]
        return ans[0]

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def helper(node):
            """
            Performs standard inorder traversal:
            left -> node -> right
            and links all nodes into DLL
            """
            nonlocal last, first
            if node:
                # left
                helper(node.left)
                # node 
                if last:
                    # link the previous node (last)
                    # with the current one (node)
                    last.right = node
                    node.left = last
                else:
                    # keep the smallest node to close DLL later on
                    first = node        
                last = node
                # right
                helper(node.right)
        
        if not root:
            return None
        
        # the smallest (first) and the largest (last) nodes
        first, last = None, None
        helper(root)
        # close DLL
        last.right = first
        first.left = last
        return first