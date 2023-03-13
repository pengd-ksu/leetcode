class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cntP = collections.Counter(p)
        cntS = collections.Counter(s[:len(p)])
        ans = []
        if cntP == cntS:
            ans.append(0)
        for i in range(1, len(s) - len(p) + 1):
            cntS[s[i-1]] -= 1
            last = s[i + len(p) - 1]
            if last in cntS:
                cntS[last] += 1
            else:
                cntS[last] = 1
            if cntS == cntP:
                ans.append(i)

        return ans