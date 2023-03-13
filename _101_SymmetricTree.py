# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric_1(self, root: Optional[TreeNode]) -> bool:
        level = [root]
        while level:
            curLevel = []
            nextLevel = []
            for node in level:
                if node:
                    curLevel.append(node.val)
                    if node.left:
                        nextLevel.append(node.left)
                    else:
                        nextLevel.append(None)
                    if node.right:
                        nextLevel.append(node.right)
                    else:
                        nextLevel.append(None)
                else:
                    curLevel.append(None)
            if curLevel != curLevel[::-1]:
                return False
            level = nextLevel
        return True

    def isSymmetric_2(self, root: Optional[TreeNode]) -> bool:
        def compareNode(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 and node2:
                return False
            if node1 and not node2:
                return False
            return node1.val == node2.val and compareNode(node1.left, node2.right) and compareNode(node1.right, node2.left)
        
        return compareNode(root.left, root.right)

    def isSymmetric_3(self, root: Optional[TreeNode]) -> bool:
        def compareNode(node1, node2):
            if not node1 and not node2:
                return True
            if node1 and node2:
                return node1.val == node2.val and compareNode(node1.left, node2.right) and compareNode(node1.right, node2.left)
            else:
                return False

        return compareNode(root.left, root.right)

    def isSymmetric_4(self, root: Optional[TreeNode]) -> bool:
        def compareNode(node1, node2):
            if node1 and node2:
                return node1.val == node2.val and compareNode(node1.left, node2.right) and compareNode(node1.right, node2.left)
            else:
                return node1 == node2

        return compareNode(root.left, root.right)

    def isSymmetric_deque(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True # In fact, there's at least one node according to constraint
        queue = collections.deque()
        queue.append((root.left, root.right))
        while queue:
            node1, node2 = queue.popleft()
            if not node1 and not node2:
                continue
            elif not node1 or not node2 or node1.val != node2.val:
                return False
            queue.append((node1.left, node2.right))
            queue.append((node1.right, node2.left))
        return True

    def isSymmetric_5(self, root: Optional[TreeNode]) -> bool:
        def EqualSubTree(l: Optional[TreeNode], r: Optional[TreeNode]) -> bool:
            if l == r == None:
                return True
            elif l == None or r == None:
                return False
            elif l.val == r.val:
                return EqualSubTree(l.left, r.right) and EqualSubTree(l.right, r.left)
            else:
                return False
        return EqualSubTree(root.left, root.right)

    def isSymmetric_recursive(self, root: Optional[TreeNode]) -> bool:
        level = [root]
        while level:
            currentLevel = []
            nextLevel = []
            for node in level:
                if node.left:
                    nextLevel.append(node.left)
                    currentLevel.append(node.left.val)
                else:
                    currentLevel.append(None)
                if node.right:
                    nextLevel.append(node.right)
                    currentLevel.append(node.right.val)
                else:
                    currentLevel.append(None)
            if currentLevel != currentLevel[::-1]:
                return False
            level = nextLevel
        return True
