from typing import List

from pytest import mark

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def inorderTraversal_1(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorderTraversal(root.left) + [root.val] + 
        self.inorderTraversal(root.right) if root else []
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        def recursive(node: Optional[TreeNode]):
            if not node:
                return
            else:
                recursive(node.left) # It's fine if node.left is None, because 
                # recursive can handle None node.
                ans.append(node.val)
                recursive(node.right) # The same as above
                
        recursive(root)
        return ans

    def inorderTraversal_stack(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        curr = root
        stack = []
        while curr != None or stack:
            while curr != None:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
        return result

    def inorderTraversal_morris(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        curr = root
        pre = TreeNode()
        while curr != None:
            if curr.left == None:
                result.append(curr.val)
                curr = curr.right
            else:
                pre = curr.left
                while pre.right != None:
                    pre = pre.right
                pre.right = curr
                temp = curr
                curr = curr.left
                temp.left = None
        return result

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        curr = root
        pre = TreeNode()
        while curr != None:
            if curr.left == None:
                result.append(curr.val)
                curr = curr.right
            else:
                pre = curr.left
                while pre.right != None:
                    pre = pre.right
                pre.right = curr
                temp = curr
                curr = curr.left
                temp.left = None
        return result