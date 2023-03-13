class Solution:
    def customSortString_peng(self, order: str, s: str) -> str:
        # This algo is only correct when translated letters are not in s.
        # Check the examples below.
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        english = {}
        for i, c in enumerate(alpha):
            english[i] = c
        forward = {}
        back = {}
        for i, c in enumerate(order):
            forward[c] = english[i]
            back[english[i]] = c
        print(f'back: {back}, forward{forward}')
        ans = ''
        for c in s:
            if c in forward.keys():
                ans += forward[c]
            else:
                ans += c
        ls = list(ans)
        ls.sort()
        print(f'ls: {ls}')
        for i in range(len(ls)):
            if ls[i] in back.keys() and back[ls[i]] in s:
                ls[i] = back[ls[i]]
        return ''.join(ls)
"""
"hucw"
"utzoampdgkalexslxoqfkdjoczajxtuhqyxvlfatmptqdsochtdzgypsfkgqwbgqbcamdqnqztaqhqanirikahtmalzqjjxtqfnh"

"hhhhhhhhhhhhhhuuuucccwwwwwweffffggggiijjjjkkkkllllmmmmnnnoooopppqqqqqqqqqqqrsssttttttttvxxxxxyyzzzzz"

"hhhhhuucccwaaaaaaaaabbdddddeffffggggiijjjjkkkkllllmmmmnnnoooopppqqqqqqqqqqqrsssttttttttvxxxxxyyzzzzz"
"""

class Solution(object):
    # The chars in order is ordered as indicated, but the rest are still in
    # the original order in s, and not changed at all
    def customSortString(self, order: str, s: str):
        # count[char] will be the number of occurrences of
        # 'char' in s.
        count = collections.Counter(s)
        ans = []

        # Write all characters that occur in order, in the order of order.
        for c in order:
            ans.append(c * count[c])
            # Set count[c] = 0 to denote that we do not need
            # to write 'c' to our answer anymore.
            count[c] = 0

        # Write all remaining characters that don't occur in order.
        # That information is specified by 'count'.
        for c in count:
            ans.append(c * count[c])

        return "".join(ans)

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        import collections
        cnt = collections.Counter(s)
        ans = ''
        for o in order:
            ans += cnt[o] * o
            cnt[o] = 0
        for c in cnt.keys(): # Must be cnt here, if loop over s, will be duplicates.
            # For example, char c could appear several times in s, every time
            # it will mutiply the its frequency.
            ans += cnt[c] * c
        return ans
