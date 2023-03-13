from typing import List
import collections

class Solution:
    def groupAnagrams_slow(strs: List[str]) -> List[List[str]]:
        ans = []
        lookup = set()
        for i in range(len(strs)):
            ct_i = collections.Counter(strs[i])
            if i not in lookup:
                lookup.add(i)
            else:
                continue
            st = []
            for j in range(i, len(strs)):
                ct_j = collections.Counter(strs[j])
                if ct_i == ct_j:
                    st.append(strs[j])
                    lookup.add(j)
            ans.append(st)
            
        return ans

    def groupAnagrams_quick(strs: List[str]) -> List[List[str]]:
        lookup = {}
        for st in strs:
            key = tuple(sorted(st))
            lookup[key] = lookup.get(key, []) + [st]
        return lookup.values()

    def groupAnagrams_3(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        lookup = defaultdict(list)
        for st in strs:
            key = tuple(sorted(st))
            lookup[key].append(st)
        return [values for values in lookup.values()]
    
if __name__ == '__main__':
    #print(groupAnagrams_slow(["eat","tea","tan","ate","nat","bat"]))
    print(groupAnagrams_quick(["eat","tea","tan","ate","nat","bat"]))
