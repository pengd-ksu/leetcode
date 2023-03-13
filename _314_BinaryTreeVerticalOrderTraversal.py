# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        queue = collections.deque()
        column = defaultdict(list)
        queue.append((root, 0))
        
        while queue:
            node, col = queue.popleft()
            if node:
                column[col].append(node.val)
                queue.append((node.left, col - 1))
                queue.append((node.right, col + 1))
        
        ans = [column[k] for k in sorted(column.keys())]
        return ans

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        # BFS without sort. The insight is that, the index accompanying
        # each node is within a range, we could return the sub-lists 
        # according to the range.
        if not root:
            return []
        queue = collections.deque()
        queue.append((root, 0))
        min_col, max_col = 0, 0
        columnTable = collections.defaultdict(list)
        
        while queue:
            node, col = queue.popleft()
            
            if node != None:
                columnTable[col].append(node.val)
                min_col = min(min_col, col)
                max_col = max(max_col, col)
                queue.append((node.left, col - 1))
                queue.append((node.right, col + 1))
                
        return [columnTable[x] for x in range(min_col, max_col + 1)]


from collections import defaultdict
class Solution:
    def verticalOrder_dfs(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        columnTable = defaultdict(list)
        min_column = max_column = 0

        def DFS(node, row, column):
            if node is not None:
                nonlocal min_column, max_column
                columnTable[column].append((row, node.val))
                min_column = min(min_column, column)
                max_column = max(max_column, column)

                # preorder DFS
                DFS(node.left, row + 1, column - 1)
                DFS(node.right, row + 1, column + 1)

        DFS(root, 0, 0)

        # order by column and sort by row
        ret = []
        for col in range(min_column, max_column + 1):
            columnTable[col].sort(key=lambda x:x[0])
            colVals = [val for row, val in columnTable[col]]
            ret.append(colVals)

        return ret