from typing import List

from pytest import mark

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, cur = [], []
        num_of_letters = 0
        for w in words:
            if num_of_letters + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    cur[i % (len(cur) - 1 or 1)] += ' '
                res.append(''.join(cur))
                cur = []
                num_of_letters = 0
            cur += [w]
            num_of_letters += len(w)
        return res + [' '.join(cur).ljust(maxWidth)]

    # 5 blanks: 0 - 4
    # 3 words, 2 spaces
    # 0 % 2 == 0
    # 1 % 2 == 1
    # 2 % 2 == 0
    # 3 % 2 == 1
    # 4 % 2 == 0

class Solution:
    def fullJustify(words: List[str], maxWidth: int) -> List[str]:
        #words for a line, one more would either exceed maxWidth or
        #leave no space among words, which should be at least 1
        #reach end of list
        lines = []
        L = 0
        while L < len(words):
            R = L
            cumulative = 0
            while R < len(words) and R - L + cumulative + len(words[R]) <= maxWidth:
                cumulative += len(words[R])
                R += 1
            if R == len(words) or R == L + 1:
                line = []
                for i in range(L, R):
                    line.append(words[i])
                    if i != R - 1:
                        line.append(' ')
                line.append(' ' * (maxWidth-cumulative-R+L+1))
                lines.append(''.join(line))
            else:
                regular_space, extra_space = divmod(maxWidth-cumulative, R-L-1)
                line = []
                line.append(words[L])
                for i in range(L+1, R):
                    if extra_space > 0:
                        extra_space -= 1
                        line.append(' ')
                    line.append(' ' * regular_space)
                    line.append(words[i])
                lines.append(''.join(line))
            L = R
        return lines

@mark.parametrize('words, maxWidth, expected', [
        (["This", "is", "an", "example", "of", "text", "justification."], 16, 
            ["This    is    an","example  of text","justification.  "]),
    ])

def test_fullJustify(words, maxWidth, expected):
    ans = Solution.fullJustify(words, maxWidth)
    assert ans == expected