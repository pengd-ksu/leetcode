class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        child = defaultdict(list)
        for i in range(len(pid)):
            child[ppid[i]].append(pid[i])
        ans = [kill]
        level = child[kill]
        while level:
            nextLevel = []
            for kid in level:
                nextLevel.extend(child[kid])
                ans.append(kid)
            level = nextLevel
        return ans

    def killProcess_2(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        child = defaultdict(list)
        for i in range(len(pid)):
            child[ppid[i]].append(pid[i])
        ans = []
        q = collections.deque()
        q.append(kill)
        while q:
            kid = q.popleft()
            ans.append(kid)
            for nxt in child[kid]:
                q.append(nxt)
        return ans