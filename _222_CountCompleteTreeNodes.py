# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # Official approach 1
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # This approach doesn't take advantage of complete binary tree
        return 1 + self.countNodes(root.left) + \
        self.countNodes(root.right) if root else 0

class Solution: # Official approach 2
    def compute_depth(self, node: TreeNode) -> int:
        """
        Return tree depth in O(d) time.
        """
        d = 0
        while node.left:
            node = node.left
            d += 1
        return d

    def exists(self, idx: int, d: int, node: TreeNode) -> bool:
        """
        Last level nodes are enumerated from 0 to 2**d - 1 (left -> right)
        Return True if last level node idx exists. 
        Binary search with O(d) complexity.
        """
        left, right = 0, 2**d - 1
        for _ in range(d):
            pivot = left + (right - left) // 2
            if idx <= pivot:
                node = node.left
                right = pivot
            else:
                node = node.right
                left = pivot + 1
        return node is not None
        
    def countNodes(self, root: TreeNode) -> int:
        # if the tree is empty
        if not root:
            return 0
        
        d = self.compute_depth(root)
        # if the tree contains 1 node
        if d == 0:
            return 1
        
        # Last level nodes are enumerated from 0 to 2**d - 1 (left -> right)
        # Perform binary search to check how many nodes exist.
        #left, right = 1, 2**d - 1
        left, right = 0, 2**d - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if self.exists(pivot, d, root):
                left = pivot + 1
            else:
                right = pivot - 1
        
        # The tree contains 2**d - 1 nodes on the first (d - 1) levels
        # and left nodes on the last level.
        return (2**d - 1) + left

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def compute_depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            return 1 + compute_depth(node.left)
        
        if not root:
            return 0
        
        left_depth = compute_depth(root.left)
        right_depth = compute_depth(root.right)
        if left_depth == right_depth:
            return (1 << left_depth) + self.countNodes(root.right)
        else:
            return self.countNodes(root.left) + (1 << right_depth)

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def getDepth(node: Optional[TreeNode], depth) -> int:
            if not node:
                return depth
            else:
                return getDepth(node.left, depth+1)
                #complete binary tree, only need to go left
                
        if not root:
            return 0
        
        leftDepth = getDepth(root.left, 0)
        rightDepth = getDepth(root.right, 0)
        if leftDepth == rightDepth:
            #the left sub is complete, and right sub is not
            #return pow(2, leftDepth) + self.countNodes(root.right)
            return (1 << leftDepth) + self.countNodes(root.right)
        else:
        #the right sub is complete, and left sub is not complete but is deeper
            #return pow(2, rightDepth) + self.countNodes(root.left)
            return (1 << rightDepth) + self.countNodes(root.left)