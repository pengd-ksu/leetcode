class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if not edges:
            return True
        parent = collections.defaultdict(list)
        for e in edges:
            parent[e[0]].append(e[1])
            parent[e[1]].append(e[0])
        frontier = parent[source]
        level = set()
        while frontier:
            nextLevel = []
            for f in frontier:
                if f == destination:
                    return True
                elif f not in level:
                    nextLevel.extend(parent[f])
                    level.add(f)
            frontier = nextLevel
        return False