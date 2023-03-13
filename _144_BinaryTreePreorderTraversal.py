# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        def preorder(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            ans.append(node.val)
            preorder(node.left)
            preorder(node.right)
            
        preorder(root)
        return ans

class Solution: # Official approach 1
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        stack, output = [root], []
        
        while stack:
            node = stack.pop()
            if node is not None:
                output.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
                
        return output

class Solution(object): # Official approach 2. Morris traversal
    def preorderTraversal(self, root):
        node, output = root, []
        while node:  
            if not node.left: 
                output.append(node.val)
                node = node.right 
            else: 
                predecessor = node.left 

                while predecessor.right and predecessor.right is not node: 
                    predecessor = predecessor.right 

                if not predecessor.right:
                    output.append(node.val)
                    predecessor.right = node  
                    node = node.left  
                else:
                    predecessor.right = None
                    node = node.right         

        return output