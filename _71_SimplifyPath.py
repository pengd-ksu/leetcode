from typing import List

from pytest import mark

class Solution:
    def simplifyPath(path: str) -> str:
        pathList = path.split('/')
        pathList = [ele.strip() for ele in pathList if ele]
        result = []
        for ele in pathList:
            if ele == '.':
                continue
            elif ele == '..':
                if result:
                    result.pop()
            else:
                result.append(ele)
        return '/' + '/'.join(result)

@mark.parametrize('path, expected', [
        ('/home/', '/home'),
        ('/../', '/'),
        ('/home//foo/', '/home/foo'),
        ('/a/./b/../../c/', '/c'),
    ])

def test_simplifyPath(path, expected):
    ans = Solution.simplifyPath(path)
    assert ans == expected