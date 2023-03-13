# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return []
        ans = []
        def preorder(node):
            if not node:
                return
            ans.append(node)
            if node.left:
                preorder(node.left)
            if node.right:
                preorder(node.right)
        preorder(root)
        for index in range(len(ans) - 1):
            ans[index].left = None
            ans[index].right = ans[index + 1]
        return root

    pre=None    
    def flatten_2(self, root):
        if root:
            self.flatten_2(root.right)
            self.flatten_2(root.left)
            root.right= self.pre
            root.left = None
            self.pre  = root

    def flatten_3(self, root: Optional[TreeNode]) -> None: 
        if root is not None:
            if root.left is not None:
                temp_right = root.right
                root.right = root.left
                self.find_rightmost_from_left_node(root.left).right = temp_right
                root.left = None
            self.flatten_3(root.right)

    def find_rightmost_from_left_node(self, node):
        while node.right is not None:
            node = node.right
        return node

    def flatten_4(self, root: Optional[TreeNode]) -> None:
        if not root:
            return root
        l = root.left
        r = root.right
        rtree = self.flatten(r)
        root.right = self.flatten(l)
        root.left = None
        node = root.right
        if node:
            while node.right:
                node = node.right
            node.right = rtree
        else:
            root.right = rtree
        return root