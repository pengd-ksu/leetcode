# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        
        level = [root]
        ans = []
        def backtrack(level):
            nonlocal ans
            currentLevel, nextLevel = [], []
            for node in level:
                if node:
                    currentLevel.append(node.val)
                    if node.left:
                        nextLevel.append(node.left)
                    if node.right:
                        nextLevel.append(node.right)
            level = nextLevel
            if level:
                backtrack(level)
            ans.append(currentLevel)
        backtrack(level)
        return ans

    def levelOrderBottom_2(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        
        level = [root]
        ans = []
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
        ans.reverse()
        return ans