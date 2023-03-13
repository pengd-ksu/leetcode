# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # Official Approach
    def successor(self, root):
        """
        One step right and then always left
        """
        root = root.right
        while root.left:
            root = root.left
        return root.val
    
    def predecessor(self, root):
        """
        One step left and then always right
        """
        root = root.left
        while root.right:
            root = root.right
        return root.val
        
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        
        # delete from the right subtree
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        # delete from the left subtree
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        # delete the current node
        else:
            # the node is a leaf
            if not (root.left or root.right):
                root = None
            # the node is not a leaf and has a right child
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            # the node is not a leaf, has no right child, and has a left child    
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
                        
        return root

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        
        rightTree = root.right
        leftTree = root.left
        
        if root.val == key:
            if rightTree is None:
                return leftTree
            elif leftTree is None:
                return rightTree
            else:
                root, node = rightTree, rightTree
                while node.left:
                    node = node.left
                node.left = leftTree
                return root
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)
        return root

class Solution: # Too naive, guess that's my initial version. Too complicated
    # to finish in an interview.
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        node = root
        prevNode = None
        while node:
            if key < node.val:
                prevNode = node
                node = node.left
            elif key > node.val:
                prevNode = node
                node = node.right
            else:#key == node.val
                if prevNode:
                    if node.left and node.right:
                        tmpLeft = node.left
                        if prevNode.val > node.val:
                            prevNode.left = node.right
                            node = node.right
                            while node.left:
                                node = node.left
                            node.left = tmpLeft
                        elif prevNode.val < node.val:
                            prevNode.right = node.right
                            node = node.right
                            while node.left:
                                node = node.left
                            node.left = tmpLeft
                    elif node.left:#node.right is None
                        if prevNode.val > node.val:
                            prevNode.left = node.left
                        elif prevNode.val < node.val:
                            prevNode.right = node.left
                    elif node.right:#node.left is None
                        if prevNode.val > node.val:
                            prevNode.left = node.right
                        elif prevNode.val < node.val:
                            prevNode.right = node.right
                    else:#node.right is None and node.left is None
                        if prevNode.val < node.val:
                            prevNode.right = None
                        else:#prevNode.val > node.val, because it's a BST
                            prevNode.left = None
                else:
                    tmpLeft = root.left
                    root = node.right
                    node = node.right
                    if node:
                        while node.left:
                            node = node.left
                        node.left = tmpLeft
                    else:
                        if tmpLeft:
                            root = tmpLeft
                        #else:
                            #return root
                return root
        return root