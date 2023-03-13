# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 0
        def recursiveSum(node: Optional[TreeNode], result) -> int:
            nonlocal ans
            if not node.left and not node.right:
                result = result * 10 + node.val
                ans += result
                return
            elif node.left and not node.right:
                recursiveSum(node.left, result * 10 + node.val)
            elif node.right and not node.left:
                recursiveSum(node.right, result * 10 + node.val)
            elif node.left and node.right:
                recursiveSum(node.left, result * 10 + node.val)
                recursiveSum(node.right, result * 10 + node.val)

        recursiveSum(root, 0)
        return ans