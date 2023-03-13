# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        if not root.left and not root.right:
            return str(root.val)
        if not root.right:
            return str(root.val) + '(' + self.tree2str(root.left) + ')'
        return str(root.val) + '(' + self.tree2str(root.left) + ')' + '(' + self.tree2str(root.right) +')'


class Solution {
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        stack = [root]
        visited = set()
        s = ''
        while stack:
            t = stack[-1]
            if t in visited:
                stack.pop()
                s += ')'
            else:
                visited.add(t);
                s += "(" + str(t.val)
                if not t.left and t.right:
                    s += "()"
                if t.right:
                    stack.append(t.right)
                if t.left:
                    stack.append(t.left)
        return s[1: len(s) - 1]