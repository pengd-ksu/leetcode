class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        seqDict = collections.defaultdict(int)
        for idx in range(len(s) - 10 + 1):
            seqDict[s[idx: idx+10]] += 1
        return [k for k, v in seqDict.items() if v > 1]

