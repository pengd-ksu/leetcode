class Solution:
    def shortestPalindrome(self, s: str) -> str:
        copyS = s[::-1]
        for i in range(len(copyS) + 1):
            if s[:len(copyS[i:])] == copyS[i:]:
                return copyS[:i] + s

    def shortestPalindrome_2(self, s: str) -> str:
        if len(s) <= 1:
            return s
        copyS = s[::-1]
        for i in range(len(copyS)):
            if s[:len(copyS[i:])] == copyS[i:]:
                return copyS[:i] + s

    def shortestPalindrome_3(self, s: str) -> str:
        if len(s) <= 1:
            return s
        copyS = s[::-1]
        for i in range(len(copyS)):
            if hash(s[:len(copyS[i:])]) == hash(copyS[i:]):#not id() here.
                if s[:len(copyS[i:])] == copyS[i:]:
                    return copyS[:i] + s