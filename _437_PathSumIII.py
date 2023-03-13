# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum_1(self, root: Optional[TreeNode], targetSum: int) -> int:
        #Can't pass large test, memeory limit exceed
        if root == None:
            return 0
        ans = []
        def dfs(node, total, path):
            if not node:
                return
            elif total + node.val == targetSum:
                path.append(node.val)
                ans.append(path)
        #Already handle null node in dfs, no need to check left and right
            dfs(node.left, total+node.val, path+[node.val])
            dfs(node.right, total+node.val, path+[node.val])
        level = [root]
        while level:
            nextLevel = []
            for node in level:
                dfs(node, 0, [])
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            level = nextLevel
        
        return len(ans)

    def pathSum_2(self, root: Optional[TreeNode], targetSum: int) -> int:
        #Get away with path, now passed all tests
        if root == None:
            return 0
        count = 0
        def dfs(node, total):
            nonlocal count
            if not node:
                return
            elif total + node.val == targetSum:
                path.append(node.val)
                count += 1
        #Already handle null node in dfs, no need to check left and right
            dfs(node.left, total+node.val)
            dfs(node.right, total+node.val)
        level = [root]
        while level:
            nextLevel = []
            for node in level:
                dfs(node, 0)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            level = nextLevel
        
        return count

    def pathSum_3(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root == None:
            return 0
        count = 0
        def dfs(node, start, total):
            nonlocal count
            if not node:
                return
            total -= node.val
            if total == 0:
                count += 1
            dfs(node.left, False, total)
            dfs(node.right, False, total)
            if start:
                dfs(node.left, True, targetSum)
                dfs(node.right, True, targetSum)
        dfs(root, True, targetSum)
        return count