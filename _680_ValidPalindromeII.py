class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while s[left] == s[right] and left <= right:
            left += 1
            right -= 1
        if left > right:
            return True
        if s[left+1:right+1] == s[left+1:right+1][::-1] or s[left: right] == s[left: right][::-1]:
            return True
        else:
            return False

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def verify(s, left, right, deleted):
            while left < right:
                if s[left] != s[right]:
                    if deleted:
                        return False
                    else:
                        return verify(s, left+1, right, True) or verify(s, left, right-1, True)
                else:
                    left += 1
                    right -= 1
            return True
        return verify(s, 0, len(s)-1, False)

class Solution:
    def validPalindrome(self, s: str) -> bool:
        # This structure is simple, and easy to control. Good for interview.
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                s1 = s[:left] + s[left+1:]
                s2 = s[:right] + s[right+1:]
                return s1 == s1[::-1] or s2 == s2[::-1]
            left += 1
            right -= 1
        return True