class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import Counter
        countS = Counter(s)
        countT = Counter(t)
        for key in countT.keys():
            if key not in countS.keys() or countT[key] != countS[key]:
                return key

    def findTheDifference_2(self, s: str, t: str) -> str:
        return chr(sum(map(ord, t)) - sum(map(ord, s)))

    def findTheDifference_3(self, s: str, t: str) -> str:
        return chr(reduce(int.__xor__, map(ord, s + t)))