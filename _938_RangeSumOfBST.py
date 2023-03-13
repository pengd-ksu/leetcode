# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if node:
                if low <= node.val <= high:
                    self.ans += node.val
                if node.val > low:
                    dfs(node.left)
                if node.val < high:
                    dfs(node.right)
                    
        self.ans = 0
        dfs(root)
        return self.ans

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        elif root.val < low or root.val > high:
            return self.rangeSumBST(root.left, low, high) +\
             self.rangeSumBST(root.right, low, high)
        else:
            return root.val + self.rangeSumBST(root.left, low, high) +\
             self.rangeSumBST(root.right, low, high)