# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        bfs = [root]
        i = 0
        while bfs[i]:
            bfs.append(bfs[i].left)
            bfs.append(bfs[i].right)
            i += 1
        return not any(bfs[i:])

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        level = [root]
        i = 0
        while level[i]:
            level.append(level[i].left)
            level.append(level[i].right)
            i += 1
        return not any(level[i:])