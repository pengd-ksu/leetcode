class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isalpha():
                if abbr[j] != word[i]:
                    return False
                i += 1
                j += 1
            else:
                if abbr[j] == '0':
                    return False
                else:
                    tmp = 0
                    while j < len(abbr) and abbr[j].isdigit():
                        tmp = tmp * 10 + int(abbr[j])
                        j += 1
                    i += tmp
        return i == len(word) and j == len(abbr)