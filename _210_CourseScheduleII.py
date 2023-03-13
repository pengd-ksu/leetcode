class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {i:set() for i in range(numCourses)}
        sequence = collections.defaultdict(set)
        for p in prerequisites:
            prereq[p[0]].add(p[1])
            sequence[p[1]].add(p[0])
        q = collections.deque([])
        for k, v in prereq.items():
            if len(v) == 0:
                q.append(k)
        taken = []
        while q:
            course = q.popleft()
            taken.append(course)
            if len(taken) == numCourses:
                return taken
            for seq in sequence[course]:
                #see sequence below. Could have several pre, need to finish them all before taking the course
                prereq[seq].remove(course)
                if not prereq[seq]:
                    q.append(seq)
        return []
        """"
        prerep:
        {0: set()}
        {1: {0}}
        {2: {0}}
        {3: {1, 2}}
        sequence:
        {null: {0}}
        {0: {1, 2}}
        {1: {3}}
        {2: {3}}
        """

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        taken = []
        prereq = {i: set() for i in range(numCourses)}
        sequence = defaultdict(list)
        
        for p in prerequisites:
            prereq[p[0]].add(p[1])
            sequence[p[1]].append(p[0])
            
        queue = collections.deque()
        for course in prereq:
            if len(prereq[course]) == 0:
                queue.append(course)
        
        while queue:
            course = queue.popleft()
            taken.append(course)
            if len(taken) == numCourses: # Ending condition check
                return taken
            for seq in sequence[course]:
                prereq[seq].remove(course)
                if len(prereq[seq]) == 0:
                    queue.append(seq)
                    
        return []

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = [0] * numCourses
        if numCourses == 0:
            return result
        
        if not prerequisites:
            result = [i for i in range(numCourses)]
            return result
        
        indegree = [0] * numCourses
        zero_degree = collections.deque()
        for p in prerequisites:
            indegree[p[0]] += 1
        for i in range(len(indegree)):
            if indegree[i] == 0:
                zero_degree.append(i)
        if not zero_degree:
            return []
        
        index = 0
        while zero_degree:
            course = zero_degree.popleft()
            result[index] = course
            index += 1
            for pre in prerequisites:
                if pre[1] == course:
                    indegree[pre[0]] -= 1
                    if indegree[pre[0]] == 0:
                        zero_degree.append(pre[0])
                        
        if any(i for i in indegree):
            return []
        return result

from collections import defaultdict
class Solution: # Official Approach 1
    WHITE = 1
    GRAY = 2
    BLACK = 3
    def findOrder(self, numCourses, prerequisites):
        # Create the adjacency list representation of the graph
        adj_list = defaultdict(list)
        # A pair [a, b] in the input represents edge from b --> a
        for dest, src in prerequisites:
            adj_list[src].append(dest)
        topological_sorted_order = []
        is_possible = True
        # By default all vertces are WHITE
        color = {k: Solution.WHITE for k in range(numCourses)}
        def dfs(node):
            nonlocal is_possible
            # Don't recurse further if we found a cycle already
            if not is_possible:
                return
            # Start the recursion
            color[node] = Solution.GRAY
            # Traverse on neighboring vertices
            if node in adj_list:
                for neighbor in adj_list[node]:
                    if color[neighbor] == Solution.WHITE:
                        dfs(neighbor)
                    elif color[neighbor] == Solution.GRAY:
                         # An edge to a GRAY vertex represents a cycle
                        is_possible = False
            # Recursion ends. We mark it as black
            color[node] = Solution.BLACK
            topological_sorted_order.append(node)

        for vertex in range(numCourses):
            # If the node is unprocessed, then call dfs on it.
            if color[vertex] == Solution.WHITE:
                dfs(vertex)
        return topological_sorted_order[::-1] if is_possible else []


from collections import defaultdict, deque
class Solution: # Official Approach 2
    def findOrder(self, numCourses, prerequisites):
        # Prepare the graph
        adj_list = defaultdict(list)
        indegree = {}
        for dest, src in prerequisites:
            adj_list[src].append(dest)
            # Record each node's in-degree
            indegree[dest] = indegree.get(dest, 0) + 1
        # Queue for maintainig list of nodes that have 0 in-degree
        zero_indegree_queue = deque([k for k in range(numCourses) if k not in indegree])

        topological_sorted_order = []

        # Until there are nodes in the Q
        while zero_indegree_queue:
            # Pop one node with 0 in-degree
            vertex = zero_indegree_queue.popleft()
            topological_sorted_order.append(vertex)
            # Reduce in-degree for all the neighbors
            if vertex in adj_list:
                for neighbor in adj_list[vertex]:
                    indegree[neighbor] -= 1
                    # Add neighbor to Q if in-degree becomes 0
                    if indegree[neighbor] == 0:
                        zero_indegree_queue.append(neighbor)

        return topological_sorted_order if len(topological_sorted_order) == numCourses else []