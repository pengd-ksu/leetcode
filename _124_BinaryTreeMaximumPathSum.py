# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #Kadane's algorithm or Maximum subarray problem
        maxSum = float('-inf')#nonlocal variable that will be iteratively updated
        
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            nonlocal maxSum
            leftMax = max(dfs(node.left), 0)#Only add positive contributors
            rightMax = max(dfs(node.right), 0)
            maxSide = max(leftMax, rightMax)
            maxSum = max(maxSum, leftMax + rightMax + node.val)
            return maxSide + node.val#Return only the max side in case
            # return duplicates
        
        dfs(root)
        return maxSum