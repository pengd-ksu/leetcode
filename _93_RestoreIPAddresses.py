from typing import List

from pytest import mark

class Solution:
    def restoreIpAddresses(s: str) -> List[str]:
        ans = []

        def backtrack(index: int, path: List[str]) -> None:
            if index > len(s) or len(path) > 4:
                return
            if index == len(s) and len(path) == 4:
                ans.append('.'.join(path))
                return
            for i in range(1,4):
                if (index + i) <= len(s) and int(s[index:index+i]) <= 255:
                    if not (s[index] == '0' and i > 1):
                        backtrack(index+i, path+[s[index:index+i]])
        backtrack(0, [])
        return ans

@mark.parametrize('s, expected', [
        ("0000", ["0.0.0.0"]),
        ("1111", ["1.1.1.1"]),
        ("010010", ['0.10.0.10', '0.100.1.0']),
        ("101023", ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"])
    ])

def test_restoreIpAddresses(s, expected):
    ans_brute = Solution.restoreIpAddresses(s)
    assert ans_brute == expected