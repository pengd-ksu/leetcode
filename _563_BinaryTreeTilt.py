# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        sumTilt = 0
        def sumSubtree(node):
            nonlocal sumTilt#See below of sumTilt
            if not node:
                return 0
            leftSum = sumSubtree(node.left)
            rightSum = sumSubtree(node.right)
            tilt = abs(leftSum - rightSum)
            sumTilt = sumTilt + tilt#The assignment makes sumTilt a local variable
            return node.val + leftSum + rightSum
        sumSubtree(root)
        return sumTilt