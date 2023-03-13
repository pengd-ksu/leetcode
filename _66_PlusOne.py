from typing import List

from pytest import mark

class Solution:
    def plusOne_power(digits: List[int]) -> List[int]:
        power, length = len(digits) - 1, len(digits) - 1
        num = 0
        new_digits = []
        while power >= 0:
            num += digits[length - power] * (10 ** power)
            power -= 1
        num += 1
        while num >= 10:
            num, r = divmod(num, 10)
            new_digits.append(r)
        new_digits.append(num)
        new_digits.reverse()
        return new_digits

    def plusOne(digits: List[int]) -> List[int]:
        s1, ans = '', []
        for i in range(len(digits)):
            s1 += str(digits[i])
        number = int(s1) + 1
        s2 = str(number)
        for num in s2:
            ans.append(int(num))
        return ans

@mark.parametrize('digits, expected', [
        ([1,2,3], [1,2,4]),
        ([4,3,2,1], [4,3,2,2]),
        ([0], [1]),
    ])

def test_plusOne(digits, expected):
    ans_power = Solution.plusOne_power(digits)
    ans = Solution.plusOne(digits)
    assert ans_power == expected
    assert ans == expected