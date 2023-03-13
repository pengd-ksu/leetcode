class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Lstr = ""
        newStr = ""
        if s:
            for i in s:
                if i not in newStr:
                    newStr = newStr + i
                else:
                    if len(newStr) > len(Lstr):
                        Lstr = newStr
                    newStr = newStr[newStr.index(i)+1:]+i
                    #newStr starts from the next after duplicate
                    #such as 'dvdf', newStr starts from 'v'
            if len(newStr) > len(Lstr):
                Lstr = newStr
            return len(Lstr)
        else:
            return 0 #check for null

    def lengthOfLongestSubstring(self, s: str) -> int:
        cur = ''
        longest = ''
        for l in s:
            if l not in cur:
                cur += l
                if len(longest) < len(cur):
                    longest = cur
            else:
                idx = cur.index(l)
                cur = cur[idx + 1:] + l#No need to check if this is the last cur, because longest so far must be longer than this one, since cur is already cut off by at least one letter.
        return len(longest)