# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        FromRight = False
        level = [root]
        ans = []
        while level:
            currentLevel = []
            nextLevel = []
            for node in level:
                currentLevel.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            if FromRight:
                currentLevel.reverse()
            ans.append(currentLevel)
            FromRight = not FromRight
            level = nextLevel
        return ans