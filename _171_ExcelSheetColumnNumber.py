class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = 0
        for letter in columnTitle:
            n = (ord(letter) - ord('A') + 1) + n * 26
        return n