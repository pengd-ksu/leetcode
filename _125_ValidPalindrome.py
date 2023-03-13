from typing import List
from pytest import mark
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ''.join([c.lower() for c in s if c.isalnum()])
        return result[::-1] == result

    def isPalindrome_re(s: str) -> bool:
        s = re.sub("[^0-9a-zA-Z]", "", s.lower())
        return s == s[::-1]

    def isPalindrome(self, s: str) -> bool:
        result = ''
        for c in s:
            if c.isalnum():
                result += c.lower()
        return result[::-1] == result

@mark.parametrize('s, expected', [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
    ])

def test_isPalindrome(s, expected):
    ans = Solution.isPalindrome(s)
    ans_re = Solution.isPalindrome_re(s)
    assert ans == expected
    assert ans_re == expected