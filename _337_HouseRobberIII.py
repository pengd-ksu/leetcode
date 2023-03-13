# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def greedrob(node):#0: not rob the house, 1: rob the house
            if not node:
                return (0, 0)
            left = greedrob(node.left)
            right = greedrob(node.right)
            #0: not rob the root, the thief could either rob its children or 
            #not; 1: rob the root, then can't rob its children
            return (max(left) + max(right), node.val + left[0] + right[0])
        return max(greedrob(root))