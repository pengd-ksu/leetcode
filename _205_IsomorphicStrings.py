class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        replaceDict = {}
        for i in range(len(s)):
            if s[i] in replaceDict.keys():
                if t[i] != replaceDict[s[i]]:
                    return False
            elif s[i] not in replaceDict.keys() and t[i] in replaceDict.values():
                return False
            elif s[i] not in replaceDict.keys():
                replaceDict[s[i]] = t[i]
        return True

    def isIsomorphic_1(self, s, t):
        s2t, t2s = {}, {}
        for i in range(len(s)):
            if s[i] in s2t and s2t[s[i]] != t[i]:
                return False
            if t[i] in t2s and t2s[t[i]] != s[i]:
                return False
            s2t[s[i]] = t[i]
            t2s[t[i]] = s[i]
        return True
    
    def transformString(self, s: str) -> str:
        index_mapping = {}
        new_str = []
        
        for i, c in enumerate(s):
            if c not in index_mapping:
                index_mapping[c] = i
            new_str.append(str(index_mapping[c]))
        
        return " ".join(new_str)
    
    def isIsomorphic_trans(self, s: str, t: str) -> bool:
        return self.transformString(s) == self.transformString(t)

    def isIsomorphic1(self, s, t):
        d1, d2 = {}, {}
        for i, val in enumerate(s):
            d1[val] = d1.get(val, []) + [i]
        for i, val in enumerate(t):
            d2[val] = d2.get(val, []) + [i]
        return sorted(d1.values()) == sorted(d2.values())
        
    def isIsomorphic2(self, s, t):
        d1, d2 = [[] for _ in range(256)], [[] for _ in range(256)]
        for i, val in enumerate(s):
            d1[ord(val)].append(i)
        for i, val in enumerate(t):
            d2[ord(val)].append(i)
        return sorted(d1) == sorted(d2)
    
    def isIsomorphic3(self, s, t):
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
    
    def isIsomorphic4(self, s, t): 
        return [s.find(i) for i in s] == [t.find(j) for j in t]
    
    def isIsomorphic5(self, s, t):
        return map(s.find, s) == map(t.find, t)

    def isIsomorphic6(self, s, t):
        d1, d2 = [0 for _ in range(256)], [0 for _ in range(256)]
        for i in range(len(s)):
            if d1[ord(s[i])] != d2[ord(t[i])]:
                return False
            d1[ord(s[i])] = i+1
            d2[ord(t[i])] = i+1
        return True