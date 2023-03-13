class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        
        #Adjacency list preparation
        neighbors = [set() for i in range(n)]
        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)
        
        leaves = [i for i in range(n) if len(neighbors[i]) == 1]
        
        #Peel out leaves
        while True:
            new_leaves = []
            
            for leaf in leaves:
                for neighbor in neighbors[leaf]:
                    neighbors[neighbor].remove(leaf)
                    if len(neighbors[neighbor]) == 1:
                        new_leaves.append(neighbor)
                
            if len(new_leaves) == 0:
                return leaves
            leaves = new_leaves

    def findMinHeightTrees_2(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        adj = [set() for _ in range(n)]
        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)

        leaves = [i for i in range(n) if len(adj[i]) == 1]

        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for i in leaves:
                j = adj[i].pop()
                adj[j].remove(i)
                if len(adj[j]) == 1:
                    newLeaves.append(j)
            leaves = newLeaves
        return leaves