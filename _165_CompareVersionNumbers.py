from typing import List

class Solution:
    def compareVersion(version1: str, version2: str) -> int:
        s1, s2 = version1.split('.'), version2.split('.')
        for i in range(len(s1)):
            if i > len(s2) - 1:
                if int(s1[i]) > 0:
                    return 1
            elif int(s1[i]) < int(s2[i]):
                return -1
            elif int(s1[i]) > int(s2[i]):
                return 1
        if len(s2) == len(s1):
            return 0
        for j in range(len(s1), len(s2)):
            if int(s2[j]) > 0:
                return -1
        return 0