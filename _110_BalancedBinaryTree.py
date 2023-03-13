# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def BST_Height(node: Optional[TreeNode]) -> int:
            if not node:
                return -1
            return 1 + max(BST_Height(node.left), BST_Height(node.right))
        
        if not root:
            return True
        return abs(BST_Height(root.left) - BST_Height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
