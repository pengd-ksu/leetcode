# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def ser_helper(node):
            if node:
                vals.append(str(node.val))
                ser_helper(node.left)
                ser_helper(node.right)
            else:
                vals.append('*')
        vals = []
        ser_helper(root)
        return ' '.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = iter(data.split())
        def deser_helper():
            v = next(vals)
            if v == '*':
                return None
            node = TreeNode(int(v))
            node.left = deser_helper()
            node.right = deser_helper()
            return node
        return deser_helper()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))