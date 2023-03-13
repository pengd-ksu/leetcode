from typing import List

from pytest import mark

class Solution:
    def lengthOfLastWord(s: str) -> int:
        last_idx = len(s) - 1
        count = 0
        while(s[last_idx]) == ' ':
            last_idx -= 1
        while(s[last_idx]) != ' ' and last_idx >= 0:
            count += 1
            last_idx -= 1
        return count

@mark.parametrize('s, expected',[
    ("Hello World", 5),
    ("   fly me   to   the moon  ", 4),
    ("luffy is still joyboy", 6),
])

def test_lengthOfLastWord(s, expected):
    ans = Solution.lengthOfLastWord(s)
    assert ans == expected