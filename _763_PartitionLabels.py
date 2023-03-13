class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        idxDict = collections.defaultdict(list)
        for i in range(len(s)):
            idxDict[s[i]].append(i)
        ans = []
        start = 0
        while start < len(s):
            last = idxDict[s[start]][-1]
            while start < last:
                start += 1
                if idxDict[s[start]][-1] > last:
                    last = idxDict[s[start]][-1]
            start += 1
            ans.append(last + 1)
        if len(ans) > 1:
            for i in range(len(ans) - 1, 0, -1):
                ans[i] = ans[i] - ans[i-1]
        return ans

    def partitionLabels_2(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s)}
        ans = []
        anchor, j = 0, 0
        for i, c in enumerate(s):
            j = max(j, last[c])
            if j == i:
                ans.append(j - anchor + 1)
                anchor = j + 1
        return ans
