# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        ans = []
        def DepthRecursive(node, result):
            if (not node.left) and (not node.right):
                result += 1
                ans.append(result)
                return
            elif node.left and (not node.right):
                DepthRecursive(node.left, result + 1)
            elif node.right and (not node.left):
                DepthRecursive(node.right, result + 1)
            elif node.left and node.right:
                DepthRecursive(node.left, result + 1)
                DepthRecursive(node.right, result + 1)
        if not root:
            return 0
        DepthRecursive(root, 0)
        return min(ans)