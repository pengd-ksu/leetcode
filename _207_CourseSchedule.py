class Solution:# Not as clear as the second one
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        import collections
        graph = defaultdict(list)
        
        for pre in prerequisites:
            graph[pre[0]].append(pre[1])
            
        visit = dict()
        
        def dfs(course):
            if course in visit.keys():
                return visit[course] # Whether True or False
            visit[course] = False
            if course in graph:
                for prereq in graph[course]:
                    if not dfs(prereq):
                        return False # visit[course] already False
            visit[course] = True
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

class Solution:# My favorite
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        import collections
        graph = collections.defaultdict(list)
        for pre in prerequisites:
            graph[pre[0]].append(pre[1])
        visited = dict()
        
        def dfs(course):
            if course in visited.keys():
                return visited[course]

            if course not in graph:
                visited[course] = True
                return True
            else:
                visited[course] = False# To handle circle
                for pre in graph[course]:
                    if not dfs(pre):
                        return False
                visited[course] = True
                return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

class Solution: # Official approach 1
    def canFinish_naive(self, numCourses, prerequisites):
        from collections import defaultdict
        courseDict = defaultdict(list)

        for relation in prerequisites:
            nextCourse, prevCourse = relation[0], relation[1]
            courseDict[prevCourse].append(nextCourse)

        path = [False] * numCourses
        for currCourse in range(numCourses):
            if self.isCyclic(currCourse, courseDict, path):
                return False
        return True

    def isCyclic(self, currCourse, courseDict, path):
        """
        backtracking method to check that no cycle would be formed 
        starting from currCourse
        """
        if path[currCourse]:
        # come across a previously visited node, i.e. detect the cycle
            return True

        # before backtracking, mark the node in the path
        path[currCourse] = True

        # backtracking
        ret = False
        for child in courseDict[currCourse]:
            ret = self.isCyclic(child, courseDict, path)
            if ret: break

        # after backtracking, remove the node from the path
        path[currCourse] = False
        return ret


class Solution: # Official approach 2
    def canFinish(self, numCourses, prerequisites):
        from collections import defaultdict
        courseDict = defaultdict(list)

        for relation in prerequisites:
            nextCourse, prevCourse = relation[0], relation[1]
            courseDict[prevCourse].append(nextCourse)
        checked = [False] * numCourses
        path = [False] * numCourses
        for currCourse in range(numCourses):
            if self.isCyclic(currCourse, courseDict, checked, path):
                return False
        return True
    def isCyclic(self, currCourse, courseDict, checked, path):
        """   """
        # 1). bottom-cases
        if checked[currCourse]:# If checked and cyclic, already return False in
            # canFinish. So there must be no cycle starting from this node. 
            # this node has been checked, no cycle would be formed with this node.
            return False
        if path[currCourse]:
            # came across a marked node in the path, cyclic !
            return True
        # 2). postorder DFS on the children nodes
        # mark the node in the path
        path[currCourse] = True
        ret = False
        # postorder DFS, to visit all its children first.
        for child in courseDict[currCourse]:
            ret = self.isCyclic(child, courseDict, checked, path)
            if ret: break
        # 3). after the visits of children, we come back to process the node itself
        # remove the node from the path
        path[currCourse] = False
        # Now that we've visited the nodes in the downstream,
        #   we complete the check of this node.
        checked[currCourse] = True
        return ret

class Solution: # Official approach 3: topological order
class GNode(object):
    """  data structure represent a vertex in the graph."""
    def __init__(self):
        self.inDegrees = 0
        self.outNodes = []

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        from collections import defaultdict, deque
        # key: index of node; value: GNode
        graph = defaultdict(GNode)

        totalDeps = 0
        for relation in prerequisites:
            nextCourse, prevCourse = relation[0], relation[1]
            graph[prevCourse].outNodes.append(nextCourse)
            graph[nextCourse].inDegrees += 1
            totalDeps += 1
        # we start from courses that have no prerequisites.
        # we could use either set, stack or queue to keep track of 
        # courses with no dependence.
        nodepCourses = deque()
        for index, node in graph.items():
            if node.inDegrees == 0:
                nodepCourses.append(index)
        removedEdges = 0
        while nodepCourses:
            # pop out course without dependency
            course = nodepCourses.pop()
            # remove its outgoing edges one by one
            for nextCourse in graph[course].outNodes:
                graph[nextCourse].inDegrees -= 1
                removedEdges += 1
                # while removing edges, we might discover new courses 
                # with prerequisites removed, i.e. new courses without 
                # prerequisites.
                if graph[nextCourse].inDegrees == 0:
                    nodepCourses.append(nextCourse)
        if removedEdges == totalDeps:
            return True
        else:
            # if there are still some edges left, then there exist 
            # some cycles. Due to the dead-lock (dependencies), we 
            # cannot remove the cyclic edges
            return False