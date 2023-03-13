from typing import List
import collections
from pytest import mark

class Solution:
    def minWindow(s: str, t: str) -> str:
        if not s or not t:
            return ""
        t_dict = collections.Counter(t)
        l, r = 0, 0
        ans = float("inf"), l, r
        window_dict = {}
        required = len(t_dict)
        formed = 0
        while r < len(s):
            character = s[r]
            window_dict[character] = window_dict.get(character, 0) + 1
            if character in t_dict and t_dict[character] == window_dict[character]:
                formed += 1
            while l <= r and formed == required:
                character = s[l]
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                window_dict[character] -= 1
                if character in t_dict and window_dict[character] < t_dict[character]:
                    formed -= 1
                l += 1
            #increase l, finally clear window_dict = {}
            r += 1
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]

    def minWindow_2(self, s: str, t: str) -> str:
        # Once tcount is established, we only care about lt, because there could
        # be duplicates in t, meaning some characters might be more than needed.
        # But the minWindow only achieved when all the frequencies are at most
        # 0, meaning there could be negatives. And once that criteria reached,
        # keep track when any character's frequency is above zero, that means 
        # not all characters in t are included in s. No need to restablish tcount
        # again.
        ls, lt = len(s), len(t)
        tcount = collections.Counter(t)
        i, j = 0, 0
        minWindow = ls + 1
        while i < ls:
            if s[i] in tcount:
                if tcount[s[i]] > 0:
                    lt -= 1
                tcount[s[i]] -= 1
            while lt == 0:
                if i - j + 1 < minWindow:
                    minWindow = i - j + 1
                    result = s[j:i+1]
                if s[j] in tcount:
                    tcount[s[j]] += 1
                    if tcount[s[j]] > 0:
                        lt += 1
                j += 1
            i += 1
        return '' if minWindow == ls + 1 else result

@mark.parametrize('s, t, expected', [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", ""),
    ])

def test_minWindow(s, t, expected):
    ans = Solution.minWindow(s, t)
    assert ans == expected