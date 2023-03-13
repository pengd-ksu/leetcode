# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth_1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth_2(self, root: Optional[TreeNode]) -> int:
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def TreeDepth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            elif (not node.right) and (not node.left):
                return 1
            elif node.right and (not node.left):
                return 1 + TreeDepth(node.right)
            elif node.left and (not node.right):
                return 1 + TreeDepth(node.left)
            elif node.right and node.left:
                return max(1 + TreeDepth(node.right), 1 + TreeDepth(node.left))
        return TreeDepth(root)

    def maxDepth_wrong(self, root: Optional[TreeNode]) -> int:
        def TreeDepth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            elif (not node.right) and (not node.left):
                return 1
            elif node.right:#if the node has both children, it will only enter right
            #and ignor the left subtree
                return 1 + TreeDepth(node.right)
            elif node.left:
                return 1 + TreeDepth(node.left)
            else:
                return max(1 + TreeDepth(node.right), 1 + TreeDepth(node.left))
        return TreeDepth(root)