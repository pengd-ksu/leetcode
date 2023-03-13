# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def path(node, res):
            if not res:
                res += str(node.val)
            else:
                res += '->' + str(node.val)
            if node.right == None and node.left == None:
                ans.append(res)
                return
            elif node.right == None:
                path(node.left, res)
            elif node.left == None:
                path(node.right, res)
            else:
                path(node.right, res)
                path(node.left, res)
        path(root, '')
        return ans