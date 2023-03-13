from typing import List
import functools
from pytest import mark

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        nodeList = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nodeList.append(node.val)
            inorder(node.right)
            
        inorder(root)
        for i in range(len(nodeList) - 1):
            if nodeList[i] >= nodeList[i+1]:
                return False
        return True