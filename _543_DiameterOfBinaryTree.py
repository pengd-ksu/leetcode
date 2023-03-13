# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def longest(node, dist):
            if not node:
                return dist
            else:
                return max(longest(node.left, dist+1), longest(node.right, dist+1))
            
        ans = 0
        level = [root]
        while level:
            nextLevel = []
            for node in level:
                ans = max(ans, longest(node.left, 0) + longest(node.right, 0))
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)
            level = nextLevel
        return ans

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def dfs(node):
            nonlocal diameter
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            diameter = max(diameter, left + right)
            return max(left, right) + 1
        dfs(root)
        return diameter