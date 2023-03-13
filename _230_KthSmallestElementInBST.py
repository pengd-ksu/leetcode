# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count, ans = 0, float('-inf')
        def inorder(node):
            nonlocal count, ans
            if node == None:
                return
            inorder(node.left)
            count += 1
            if count == k:
                ans = node.val
                return
            inorder(node.right)
        inorder(root)
        return ans

    def kthSmallest_recursive(self, root: Optional[TreeNode], k: int) -> int:
            def inorder(node):
                return inorder(node.left) + [node.val] + inorder(node.right) if node else []
            return inorder(root)[k - 1]

    def kthSmallest_iterative(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right