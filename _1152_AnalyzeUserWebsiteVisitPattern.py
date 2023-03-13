class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        by_user = defaultdict(list)
        for t, u, w in sorted(zip(timestamp, username, website)):
            by_user[u].append(w)

        cnt = Counter()
        for x in by_user.values():
            cnt += Counter(set(combinations(x, 3)))

        return min(cnt, key=lambda k: (-cnt[k], k))

"""
combinations: 
https://docs.python.org/3/library/itertools.html#itertools.combinations

itertools.combinations(iterable, r)
Return r length subsequences of elements from the input iterable.

The combination tuples are emitted in lexicographic ordering according 
to the order of the input iterable. So, if the input iterable is sorted, 
the combination tuples will be produced in sorted order.
"""

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        dp = collections.defaultdict(list)
        for t, u, w in sorted(zip(timestamp, username, website)):
            dp[u].append(w)
        count = sum([collections.Counter(set(itertools.combinations(dp[u], 3))) for u in dp], collections.Counter())
        return list(min(count, key=lambda k: (-count[k], k)))