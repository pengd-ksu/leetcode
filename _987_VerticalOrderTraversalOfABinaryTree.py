# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        #nlog(n/k), k is the width, or the columns.
        import collections
        q = collections.deque()
        q.append((root, 0, 0))
        nodedict = defaultdict(list)
        minc = float('inf')
        maxc = float('-inf')
        while q:
            node, row, col = q.popleft()
            minc = min(minc, col)
            maxc = max(maxc, col)
            nodedict[col].append((row, node.val))
            if node.left:
                q.append((node.left, row + 1, col - 1))
            if node.right:
                q.append((node.right, row + 1, col + 1))
        ans = []
        for col in range(minc, maxc + 1):
            ans.append([val for row, val in sorted(nodedict[col])])
        return ans

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        import collections
        queue = collections.deque()
        row, col = 0, 0
        queue.append((root, row, col))
        nodeList = []
        minCol, maxCol = 0, 0
        while queue:
            node, row, col = queue.pop()
            minCol = min(minCol, col)
            maxCol = max(maxCol, col)
            nodeList.append((col, row, node.val))#priority: col > row > val
            if node.left:
                queue.append((node.left, row+1, col-1))
            if node.right:
                queue.append((node.right, row+1, col+1))
        nodeList.sort()# The sorting will be ordered by the three priorities
        nodeDic = collections.defaultdict(list)
        for col, row, val in nodeList:
            nodeDic[col].append(val)
        return [nodeDic[col] for col in range(minCol, maxCol+1)]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        node_list = []

        def BFS(root):
            queue = deque([(root, 0, 0)])
            while queue:
                node, row, column = queue.popleft()
                if node is not None:
                    node_list.append((column, row, node.val))
                    queue.append((node.left, row + 1, column - 1))
                    queue.append((node.right, row + 1, column + 1))

        # step 1). construct the global node list, with the coordinates
        BFS(root)

        # step 2). sort the global node list, according to the coordinates
        node_list.sort()

        # step 3). retrieve the sorted results partitioned by the column index
        ret = OrderedDict()
        for column, row, value in node_list:
            if column in ret:
                ret[column].append(value)
            else:
                ret[column] = [value]

        return ret.values()

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        node_list = []

        def DFS(node, row, column):
            if node is not None:
                node_list.append((column, row, node.val))
                # preorder DFS
                DFS(node.left, row + 1, column - 1)
                DFS(node.right, row + 1, column + 1)

        # step 1). construct the node list, with the coordinates
        DFS(root, 0, 0)

        # step 2). sort the node list globally, according to the coordinates
        node_list.sort()

        # step 3). retrieve the sorted results grouped by the column index
        ret = []
        curr_column_index = node_list[0][0]
        curr_column = []
        for column, row, value in node_list:
            if column == curr_column_index:
                curr_column.append(value)
            else:
                # end of a column, and start the next column
                ret.append(curr_column)
                curr_column_index = column
                curr_column = [value]
        # add the last column
        ret.append(curr_column)

        return ret


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        columnTable = defaultdict(list)
        min_column = max_column = 0

        def BFS(root):
            nonlocal min_column, max_column
            queue = deque([(root, 0, 0)])

            while queue:
                node, row, column = queue.popleft()

                if node is not None:
                    columnTable[column].append((row, node.val))
                    min_column = min(min_column, column)
                    max_column = max(max_column, column)

                    queue.append((node.left, row + 1, column - 1))
                    queue.append((node.right, row + 1, column + 1))

        # step 1). BFS traversal
        BFS(root)

        # step 2). extract the values from the columnTable
        ret = []
        for col in range(min_column, max_column + 1):
            # sort first by 'row', then by 'value', in ascending order
            ret.append([val for row, val in sorted(columnTable[col])])

        return ret


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
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

        # step 1). DFS traversal
        DFS(root, 0, 0)

        # step 2). extract the values from the columnTable
        ret = []
        for col in range(min_column, max_column + 1):
            # sort first by 'row', then by 'value', in ascending order
            ret.append([val for row, val in sorted(columnTable[col])])

        return ret