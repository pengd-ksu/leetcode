# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        ans = []
        level = [root]
        while level:
            currentLevel, nextLevel = [], []
            for node in level:
                currentLevel.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            ans.append(currentLevel)
            level = nextLevel
        return ans

    def levelOrder_2(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        result = []
        level = [root]
        while level:
            result.append([node.val for node in level])
            level = [kid for node in level for kid in (node.left, node.right) if kid]
        return result