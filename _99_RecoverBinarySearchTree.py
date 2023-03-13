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
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        3 - 2 - 1
        1 - 2 - 3
        """
        ans = []
        
        def preorder(node):
            if node is not None:
                preorder(node.left)
                ans.append(node)
                preorder(node.right)
                
        preorder(root)
        start, end = 0, len(ans) - 1
        while ans[start].val < ans[start + 1].val:
            start += 1
        while ans[end].val > ans[end - 1].val:
            end -= 1
        ans[start].val, ans[end].val = ans[end].val, ans[start].val

class Solution: # Official Approach 1
    def recoverTree(self, root: TreeNode):
        def inorder(r: TreeNode) -> List[int]:
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        
        def find_two_swapped(nums: List[int]) -> (int, int):
            n = len(nums)
            x = y = None 
            # Initialize x and y as a value that cannot be the value of a node.
            for i in range(n - 1):
                if nums[i + 1] < nums[i]:
                    y = nums[i + 1]
                    # first swap occurrence
                    if x is None:     
                        x = nums[i]
                    # second swap occurrence
                    else:           
                        break
            return x, y
        
        def recover(r: TreeNode, count: int):
            if r:
                if r.val == x or r.val == y:
                    r.val = y if r.val == x else x
                    count -= 1
                    if count == 0:
                        return      
                recover(r.left, count)
                recover(r.right, count)
            
        nums = inorder(root)
        x, y = find_two_swapped(nums)
        recover(root, 2)

class Solution: # Official Approach 2
    def recoverTree(self, root: TreeNode):
        """
        :rtype: void Do not return anything, modify root in-place instead.
        """
        stack = []
        x = y = pred = None
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pred and root.val < pred.val:
                y = root
                if x is None:
                    x = pred 
                else:
                    break
            pred = root
            root = root.right

        x.val, y.val = y.val, x.val

class Solution: # Official Approach 3
    def recoverTree(self, root):
        def find_two_swapped(root: TreeNode):
            nonlocal x, y, pred
            if root is None:
                return
            
            find_two_swapped(root.left)
            if pred and root.val < pred.val:
                y = root
                # first swap occurence
                if x is None:
                    x = pred 
                # second swap occurence
                else:
                    return
            pred = root
            find_two_swapped(root.right)
        
        x = y = pred = None
        find_two_swapped(root)
        x.val, y.val = y.val, x.val

class Solution: # Official Approach 4
    def recoverTree(self, root):
        # predecessor is a Morris predecessor. 
        # In the 'loop' cases it could be equal to the node itself 
        # predecessor == root. pred is a 'true' predecessor, 
        # the previous node in the inorder traversal.
        x = y = predecessor = pred = None
        
        while root:
            # If there is a left child
            # then compute the predecessor.
            # If there is no link predecessor.right = root --> set it.
            # If there is a link predecessor.right = root --> break it.
            if root.left:       
                # Predecessor node is one step left 
                # and then right till you can.
                predecessor = root.left
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right
 
                # set link predecessor.right = root
                # and go to explore left subtree
                if predecessor.right is None:
                    predecessor.right = root
                    root = root.left
                # break link predecessor.right = root
                # link is broken : time to change subtree and go right
                else:
                    # check for the swapped nodes
                    if pred and root.val < pred.val:
                        y = root
                        if x is None:
                            x = pred 
                    pred = root
                    
                    predecessor.right = None
                    root = root.right
            # If there is no left child
            # then just go right.
            else:
                # check for the swapped nodes
                if pred and root.val < pred.val:
                    y = root
                    if x is None:
                        x = pred 
                pred = root
                
                root = root.right
        
        x.val, y.val = y.val, x.val