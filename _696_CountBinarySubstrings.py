class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans, prev, cur = 0, 0, 1
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                ans += min(prev, cur)#First one will be zero
                prev = cur
                cur = 1
            else:
                cur += 1
        ans += min(prev, cur)
        return ans


"""
We can convert the string s into an array groups that represents the length 
of same-character contiguous blocks within the string. For example, if 
s = "110001111000000", then groups = [2, 3, 4, 6].

For every binary string of the form '0' * k + '1' * k or '1' * k + '0' * k, 
the middle of this string must occur between two groups.

Let's try to count the number of valid binary strings between groups[i] and 
groups[i+1]. If we have groups[i] = 2, groups[i+1] = 3, then it represents 
either "00111" or "11000". We clearly can make min(groups[i], groups[i+1]) 
valid binary strings within this string. Because the binary digits to the 
left or right of this string must change at the boundary, our answer can 
ever be larger.
"""
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = [1]
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                groups.append(1)
            else:
                groups[-1] += 1
                
        ans = 0
        for i in range(1, len(groups)):
            ans += min(groups[i-1], groups[i])
        return ans

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = [len(list(v)) for _, v in itertools.groupby(s)]
        return sum(min(a, b) for a, b in zip(groups, groups[1:]))