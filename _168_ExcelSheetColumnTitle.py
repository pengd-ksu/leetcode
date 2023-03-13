class Solution:
    def convertToTitle(columnNumber: int) -> str:
        ans = ''
        while columnNumber:
            columnNumber -= 1
            columnNumber, r = divmod(columnNumber, 26)
            ans += chr(r + ord('A'))
        return ans[::-1]