# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Key: nodes with same height should be stored in the same list
        # The height of a node is the length of the longest downward
        # path to a leaf from that node. 
        output = defaultdict(list)
        
        def dfs(node: Optional[TreeNode], layer: int) -> int:
            if not node:
                return 0
            left = dfs(node.left, layer)
            right = dfs(node.right, layer)
            layer = max(left, right)
            output[layer+1].append(node.val)
            return layer + 1
        
        dfs(root, 0)
        return output.values()