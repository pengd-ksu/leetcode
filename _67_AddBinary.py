from typing import List
from pytest import mark

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ''
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or carry > 0:
            if i < 0:
                s1 = '0'
            else:
                s1 = a[i]
            if j < 0:
                s2 = '0'
            else:
                s2 = b[j]
            carry, rem = divmod(int(s1)+int(s2)+carry, 2)
            ans = str(rem) + ans
            i -= 1
            j -= 1
        return ans

    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]

    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)
        
        carry = 0
        answer = []
        for i in range(n - 1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1
                
            if carry % 2 == 1:
                answer.append('1')
            else:
                answer.append('0')
            
            carry //= 2
        
        if carry == 1:
            answer.append('1')
        answer.reverse()
        return ''.join(answer)

    def addBinary(self, a: str, b: str) -> str:
        return '{0:b}'.format(int(a, 2) + int(b, 2))

    def addBinary_bit(a: str, b: str) -> str:
        # ^(xor) for carry, &(and) for this digit
        x, y = int(a, 2), int(b, 2)
        answer = x ^ y
        carry = (x & y) << 1
        answer = answer + carry
        return bin(answer)[2:]

    def addBinary_builtin(a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)
        return bin(x + y)[2:]

    def addBinary(a: str, b: str) -> str:
        x, y = 0, 0
        for i in range(len(a)):
            x = int(a[i]) + x * 2
        for j in range(len(b)):
            y = int(b[j]) + y * 2
        sum_ab = x + y
        ans = ''
        if sum_ab == 0:
            return '0'
        while sum_ab > 0:
            ans = str(sum_ab % 2) + ans#Just like to get decimal
            sum_ab //= 2
        return ans

@mark.parametrize('a, b, expected', [
        ("11", "1", "100"),
        ("1010", "1011", "10101"),
    ])

def test_addBinary(a, b, expected):
    ans_bit = Solution.addBinary_bit(a, b)
    ans_builtin = Solution.addBinary_builtin(a, b)
    ans = Solution.addBinary(a, b)
    assert ans_bit == expected
    assert ans_builtin == expected
    assert ans == expected