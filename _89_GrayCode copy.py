from typing import List
from pytest import mark

class Solution:
    def grayCode(n: int) -> List[int]:
        if n == 1:
            return [0, 1]
        if n > 1:
            prev = Solution.grayCode(n - 1)
            s = '{' + f'0:0{n - 1}b' + '}'
            #'{0:04b}'.format(4) -> '0100', can set # of bits in binary
            prev = [s.format(ele) for ele in prev]
            prev = [str(ele) for ele in prev]
            cur = prev.copy()
            prev_reverse = [ele for ele in prev[::-1]]
            cur = ['0' + ele for ele in cur]
            prev_reverse = ['1' + ele for ele in prev_reverse]
            cur = cur + prev_reverse
        return [int(ele, 2) for ele in cur]
    #Check https://en.wikipedia.org/wiki/Gray_code on how to construct it

    def grayCode_binary(n: int) -> List[int]:
        return [i ^ (i >> 1) for i in range(1 << n)]
    #Check https://en.wikipedia.org/wiki/Gray_code for binary conversion

@mark.parametrize('n, expected', [
        (2, [0,1,3,2]),
        (1, [0,1]),
        (3, [0, 1, 3, 2, 6, 7, 5, 4]),
    ])

def test_grayCode(n, expected):
    ans = Solution.grayCode(n)
    ans_bin = Solution.grayCode_binary(n)
    assert ans == expected
    assert ans_bin == expected