# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        rightside = []
        
        def dfs(node: TreeNode, level: int) -> None:
            if level == len(rightside):
            # This step is to choose whichever comes first from the right-side view. If the right child has no descendant, then the left child (if existed) will have its right child chosen.
                rightside.append(node.val)
            for child in [node.right, node.left]:# right first
                if child:
                    dfs(child, level + 1)
                    
        dfs(root, 0)
        return rightside

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        view = []
        if root:
            level = [root]
            while level:
                view += [level[-1].val]#view += level[-1].val,#This is also right
                level = [kid for node in level for kid in (node.left, node.right) if kid]
        return view

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        view = []
        if not root:
            return view
        
        level = [root]
        while level:
            nextLevel = []
            view.append(level[-1].val)
            for node in level:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            level = nextLevel
        return view

    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        next_level = deque([root,])
        rightside = []
        
        while next_level:
            # prepare for the next level
            curr_level = next_level
            next_level = deque()

            while curr_level:
                node = curr_level.popleft()
                    
                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            # The current level is finished.
            # Its last element is the rightmost one.
            rightside.append(node.val)
        
        return rightside

    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        queue = deque([root])
        rightside = []
        
        while queue:
            level_length = len(queue)

            for i in range(level_length):
                node = queue.popleft()
                # if it's the rightmost element
                if i == level_length - 1:
                    rightside.append(node.val)
                    
                # add child nodes in the queue 
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return rightside

    def rightSideView_2(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        right = self.rightSideView(root.right)
        left = self.rightSideView(root.left)
        return [root.val] + right + left[len(right):]
    #consider this: a=[1], a[1:] is []. So right will cover all the spots when it's 
    #available. But left will appear when right runs out. And the right part in 
    #the left will appear whenever it's possible.

    def rightSideView_3(self, root: Optional[TreeNode]) -> List[int]:
        def collect(node, depth):
            if node:
                if depth == len(view):
                    view.append(node.val)
                collect(node.right, depth+1)#right comes first. It will fill view first.
                collect(node.left, depth+1)
        view = []
        collect(root, 0)
        return view