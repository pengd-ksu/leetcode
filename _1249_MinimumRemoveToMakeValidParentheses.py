class Solution:#remove as a list will cost linear time in searching in last step
    def minRemoveToMakeValid(self, s: str) -> str:
        # Keep a set to record whichever is left over as invalid parantheses
        remove = []
        for i, c in enumerate(s):
            if c not in '()':
                continue
            elif c == '(':
                remove.append(i)
            else:
                if remove and s[remove[-1]] == '(':
                    remove.pop()
                else:
                    remove.append(i)
        ans = ''
        for i, c in enumerate(s):
            if i not in remove:
                ans += c
        return ans

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Keep a set to record whichever is left over as invalid parantheses
        remove = []
        for i, c in enumerate(s):
            if c not in '()':
                continue
            elif c == '(':
                remove.append(i)
            else:
                if remove and s[remove[-1]] == '(':
                    remove.pop()
                else:
                    remove.append(i)
        removeSet = set()
        while remove:
            removeSet.add(remove.pop())
        ans = ''
        for i, c in enumerate(s):
            if i not in removeSet:
                ans += c
        return ans

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Keep a set to record whichever is left over as invalid parantheses
        remove = []
        for i, c in enumerate(s):
            if c not in '()':
                continue
            elif c == '(':
                remove.append(i)
            else:
                if remove and s[remove[-1]] == '(':
                    remove.pop()
                else:
                    remove.append(i)
        removeSet = set(remove)
        ans = ''
        for i, c in enumerate(s):
            if i not in removeSet:
                ans += c
        return ans