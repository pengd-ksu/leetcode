# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def array_to_tree(left, right):
            nonlocal postorder_index
            if left > right:
                return None
            root_value = postorder[postorder_index]
            root = TreeNode(root_value)
            
            postorder_index -= 1
            root.right = array_to_tree(inorder_index_map[root_value] + 1, right)
            root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
            return root
            
        postorder_index = len(postorder) - 1
        
        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index
            
        return array_to_tree(0, len(postorder) - 1)

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:       
        def array_to_tree(left, right):
            nonlocal preorder_index
            # if there are no elements to construct the tree
            if left > right: return None

            # select the preorder_index element as the root and increment it
            root_value = preorder[preorder_index]
            root = TreeNode(root_value)

            preorder_index += 1

            # build left and right subtree
            # excluding inorder_index_map[root_value] element because it's the root
            root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
            root.right = array_to_tree(inorder_index_map[root_value] + 1, right)

            return root

        preorder_index = 0

        # build a hashmap to store value -> its index relations
        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index

        return array_to_tree(0, len(preorder) - 1)