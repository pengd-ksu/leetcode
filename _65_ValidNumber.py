from typing import List

from pytest import mark
import unittest

class Solution:
    def isNumber_1(self, s: str) -> bool:
        seen_digit = seen_exponent = seen_dot = False
        for i, c in enumerate(s):
            if c.isdigit():
                seen_digit = True
            elif c in ['+', '-']:
                if i > 0 and s[i-1] != 'e' and s[i-1] != 'E':
                    return False
            elif c in ['e', 'E']:
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                seen_digit = False#Construct new integers after 'E' or 'e'
            elif c == '.':
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            else:
                return False
        return seen_digit

class Solution:
    def isNumber_DFA(self, s):
        # This is the DFA we have designed above
        dfa = [
            {"digit": 1, "sign": 2, "dot": 3},
            {"digit": 1, "dot": 4, "exponent": 5},
            {"digit": 1, "dot": 3},
            {"digit": 4},
            {"digit": 4, "exponent": 5},
            {"sign": 6, "digit": 7},
            {"digit": 7},
            {"digit": 7}
        ]
        
        current_state = 0
        for c in s:
            if c.isdigit():
                group = "digit"
            elif c in ["+", "-"]:
                group = "sign"
            elif c in ["e", "E"]:
                group = "exponent"
            elif c == ".":
                group = "dot"
            else:
                return False

            if group not in dfa[current_state]:
                return False
            
            current_state = dfa[current_state][group]
        
        return current_state in [1, 4, 7]

class Solution:
#Integer and Decimal must be separately because an 'e' or 'E', 
#can only be followed by an integer.
    def isNumber_peng(s: str) -> bool:
        def isDecimal(s: str) -> bool:
            if not s:
                return False
            elif s[0] == '+' or s[0] == '-':
                if len(s) > 1:
                    s = s[1:]
                else:
                    return False
            
            _count = 0
            hasNumber = False
            for ele in s:
                if ele == '.':
                    _count += 1
                elif ele.isdigit():
                    hasNumber = True#'+.' is not valid
                else:
                    return False
            if _count > 1:
                return False
            return hasNumber
                        
        def isInteger(s: str) -> bool:
            if not s:
                return False
            elif s[0] == '+' or s[0] == '-':
                if len(s) > 1:
                    s = s[1:]
                else:
                    return False
            for ele in s:
                if not ele.isdigit():
                    return False
            return True
        
        e_index = 0
        if 'e' in s or 'E' in s:
            for ele in s:
                if ele != 'e' and ele != 'E':
                    e_index += 1
                else:
                    break
            return (isDecimal(s[0:e_index]) or isInteger(s[0:e_index])) and isInteger(s[e_index+1:])
            #before 'e' or 'E'
            #after 'e' or 'E'. False if nothing follows, or following thing
            #not integer
        else:
            #test integer or decimal
            return (isDecimal(s) or isInteger(s))

@mark.parametrize('string, expected',[
    ('0', True),
    ('e', False),
    ('.', False),
    ('.1', True)
])

def test_isNumber(string, expected):
    ans = Solution.isNumber(string)
    assert ans == expected