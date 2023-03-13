# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def PathSum(node: Optional[TreeNode], result: int) -> bool:
            if (not node.left) and (not node.right):
                result += node.val
                print(f"result == targetSum: {result == targetSum}")
                return result == targetSum

            elif node.left and (not node.right):
                print(f"Turn Left, {result + node.val}")
                return PathSum(node.left, result + node.val)
            elif node.right and (not node.left):
                print(f"Turn Right, {result + node.val}")
                return PathSum(node.right, result + node.val)
            elif node.left and node.right:
                print("Left and right")
                return PathSum(node.right, result + node.val) or PathSum(node.left, result + node.val)
        
        if not root:
            print("Null root")
            return False
        return PathSum(root, 0)
        