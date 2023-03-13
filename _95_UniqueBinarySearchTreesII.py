from typing import List
from typing import Optional
from pytest import mark

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(n: int) -> List[Optional[TreeNode]]:
        start, end = 1, n
        
        def RecurTree(start: int, end: int):
            if start > end:
                return [None]
            if start == end:
                return [TreeNode(start)]
            result = []
            for i in range(start, end + 1):
                left = RecurTree(start, i - 1)
                right = RecurTree(i + 1, end)
                for l in left:
                    for r in right:
                        tmp = TreeNode(i)
                        tmp.left = l
                        tmp.right = r
                        result.append(tmp)
            return result

        return RecurTree(start, end)
