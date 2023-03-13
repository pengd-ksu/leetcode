

class Solution: # DFS
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        def dfs(node, elapsed):
        # If some signal arrived earlier, we don't need to broadcast it 
        # anymore. Otherwise, we should broadcast the signal. Important pruning.
            if elapsed >= dist[node]:
                return
            dist[node] = elapsed
            for time, neighbour in sorted(graph[node]):
                dfs(neighbour, elapsed + time)

        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))
        dist = {node: float('inf') for node in range(1, n + 1)}
        dfs(k, 0)
        ans = max(dist.values())
        return ans if ans < float('inf') else -1

class Solution: # BFS
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 0 in index zero to keep largest element less than infinity if 
        # solution exists
        elapsedTime = [0] + [float('inf')] * n
        queue = collections.deque()
        queue.append((0, k))
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        while queue:
            time, node = queue.popleft()
            if time < elapsedTime[node]:
                elapsedTime[node] = time
                for v, w in graph[node]:
                    queue.append((time + w, v))
        
        ans = max(elapsedTime)
        return ans if ans < float('inf') else -1

# Dijkstra algorithm
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        elapsedTime = [0] + [float('inf')] * n
        graph = defaultdict(list)
        heap = [(0, k)]
        for source, destination, cost in times:
            graph[source].append((destination, cost))
        while heap:
            time, source = heapq.heappop(heap)
            if time < elapsedTime[source]:
                elapsedTime[source] = time
                for destination, cost in graph[source]:
                    heapq.heappush(heap, (time + cost, destination))
        ans = max(elapsedTime)
        return ans if ans < float('inf') else -1

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #Dijkstra's algorithm
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        dist = {node: float('inf') for node in range(1, n+1)}
        seen = [False] * (n+1)
        dist[k] = 0
        while True:
            cand_node = -1
            cand_dist = float('inf')
            for i in range(1, n+1):
                if not seen[i] and dist[i] < cand_dist:
                    cand_dist = dist[i]
                    cand_node = i
            
            if cand_node < 0:
                break
            seen[cand_node] = True
            for nei, d in graph[cand_node]:
                dist[nei] = min(dist[nei], dist[cand_node] + d)
                
        ans = max(dist.values())
        return ans if ans < float('inf') else -1


# https://leetcode.com/problems/network-delay-time/discuss/471164/Python-DFS-BFS-Dijkstra-Bellman-Ford-SPFA-Floyd-Warshall
import heapq
from collections import deque
from collections import defaultdict

# """
#  Uses simple DFS - Accepted
class Solution(object):
    def networkDelayTime(self, times, N, K):
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        distance = {node: float("inf") for node in range(1, N + 1)}
        self.DFS(graph, distance, K, 0)
        totalTime = max(distance.values())
        return totalTime if totalTime < float("inf") else -1

    def DFS(self, graph, distance, node, elapsedTimeSoFar):
        if elapsedTimeSoFar >= distance[node]:   # signal aalreaady reached to this node. so no need to explore for this node
            return
        distance[node] = elapsedTimeSoFar
        for neighbour, time in sorted(graph[node]):
            self.DFS(graph, distance, neighbour, elapsedTimeSoFar + time)
# """

# """
#  Uses simple BFS - Accepted
class Solution:
    def networkDelayTime(self, times, N, K):
        elapsedTime, graph, queue = [0] + [float("inf")] * N, defaultdict(list), deque([(0, K)])
        for u, v, w in times:
            graph[u].append((v, w))
        while queue:
            time, node = queue.popleft()
            if time < elapsedTime[node]:
                elapsedTime[node] = time
                for v, w in graph[node]:
                    queue.append((time + w, v))
        mx = max(elapsedTime)
        return mx if mx < float("inf") else -1
# """

# """
# Dijkstra algorithm - Accepted
class Solution:
    def networkDelayTime(self, times, N, K):
        elapsedTime, graph, heap = [0] + [float("inf")] * N, defaultdict(list), [(0, K)] # it's a min-heap
        for u, v, w in times:
            graph[u].append((v, w))
        while heap:
            time, node = heapq.heappop()
            if time < elapsedTime[node]:
                elapsedTime[node] = time
                for v, w in graph[node]:
                    heapq.heappush(heap, (time + w, v))
        mx = max(elapsedTime)
        return mx if mx < float("inf") else -1
# """

# """
# Original Bellman–Ford algorithm - Accepted
class Solution:
    def networkDelayTime(self, times, N, K):
        distance = [float("inf") for _ in range(N)]
        distance[K-1] = 0
        for _ in range(N-1):
            for u, v, w in times:
                if distance[u-1] + w < distance[v-1]:
                    distance[v-1] = distance[u-1] + w
        return max(distance) if max(distance) < float("inf") else -1
# """

# """
# Shortest Path Faster Algorithm (SPFA): An improvement of the Bellman–Ford algorithm - Accepted
class Solution:
    def networkDelayTime(self, times, N, K):
        elapsedTime, graph, queue = [0] + [float("inf")] * N, defaultdict(list), deque([(0, K)])
        elapsedTime[K] = 0
        for u, v, w in times:
            graph[u].append((v, w))
        while queue:
            time, node = queue.popleft()
            for neighbour in graph[node]:
                v, w = neighbour
                if time + w < elapsedTime[v]:
                    elapsedTime[v] = time + w
                    queue.append((time + w, v))
        mx = max(elapsedTime)
        return mx if mx < float("inf") else -1
# """

# """
#  Floyd Warshall - Accepted
class Solution:
    def networkDelayTime(self, times, N, K):
        elapsedTimeMatrix = [[float("inf") for _ in range(N)] for _ in range(N)]
        for u, v, w in times:
            elapsedTimeMatrix[u - 1][v - 1] = w
        for i in range(N):                      #   Assigning 0 to the diagonal cells
            elapsedTimeMatrix[i][i] = 0
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    elapsedTimeMatrix[i][j] = min(elapsedTimeMatrix[i][j], elapsedTimeMatrix[i][k] + elapsedTimeMatrix[k][j])
        mx = max(elapsedTimeMatrix[K - 1])
        return mx if mx < float("inf") else -1
# """

# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph
class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
 
    def printSolution(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(node, "\t\t", dist[node])
 
    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):
 
        # Initialize minimum distance for next node
        min = 1e7
 
        # Search not nearest vertex not in the
        # shortest path tree
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
 
        return min_index
 
    # Function that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):
 
        dist = [1e7] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
 
        for cout in range(self.V):
 
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minDistance(dist, sptSet)
 
            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[u] = True
 
            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.V):
                if (self.graph[u][v] > 0 and
                   sptSet[v] == False and
                   dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]
 
        self.printSolution(dist)
 
# Driver program
g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]
 
g.dijkstra(0)


import sys
 
class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
        
    def construct_graph(self, nodes, init_graph):
        '''
        This method makes sure that the graph is symmetrical. In other words, if there's a path from node A to B with a value V, there needs to be a path from node B to node A with a value V.
        '''
        graph = {}
        for node in nodes:
            graph[node] = {}
        
        graph.update(init_graph)
        
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
                    
        return graph
    
    def get_nodes(self):
        "Returns the nodes of the graph."
        return self.nodes
    
    def get_outgoing_edges(self, node):
        "Returns the neighbors of a node."
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    
    def value(self, node1, node2):
        "Returns the value of an edge between two nodes."
        return self.graph[node1][node2]

def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())
 
    # We'll use this dict to save the cost of visiting each node and update it as we move along the graph   
    shortest_path = {}
 
    # We'll use this dict to save the shortest known path to a node found so far
    previous_nodes = {}
 
    # We'll use max_value to initialize the "infinity" value of the unvisited nodes   
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # However, we initialize the starting node's value with 0   
    shortest_path[start_node] = 0
    
    # The algorithm executes until we visit all nodes
    while unvisited_nodes:
        # The code block below finds the node with the lowest score
        current_min_node = None
        for node in unvisited_nodes: # Iterate over the nodes
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
                
        # The code block below retrieves the current node's neighbors and updates their distances
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node
 
        # After visiting its neighbors, we mark the node as "visited"
        unvisited_nodes.remove(current_min_node)
    
    return previous_nodes, shortest_path


def dijkstra(graph, start_vertex):
    D = {v:float('inf') for v in range(graph.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D