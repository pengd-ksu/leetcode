# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')
        check = 0 # Root as 0, 1 for left and 2 for right
        
        def recurse(node, check, count):
            nonlocal ans
            if node:
                if check == 1:
                    recurse(node.left, 2, count + 1)
                    recurse(node.right, 1, 0)
                elif check == 2:
                    recurse(node.right, 1, count + 1)
                    recurse(node.left, 2, 0)
                else:
                    recurse(node.left, 2, 0)
                    recurse(node.right, 1, 0)
            else:
                ans = max(ans, count)
                
        recurse(root, 0, 0)
        return ans


    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')
        
        def recurse(node):
            nonlocal ans
            if not node:
                return (-1, -1) # visited nodes minus 1
            l1, r1 = recurse(node.left)
            l2, r2 = recurse(node.right)
            #Go to left, then next step must go right; Got to right,
            # next step must go left
            ans = max(ans, max(r1 + 1, l2 + 1))
            return (r1 + 1, l2 + 1)
        
        recurse(root)
        return ans