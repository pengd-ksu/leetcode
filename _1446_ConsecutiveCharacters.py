class Solution:
    def maxPower(self, s: str) -> int:
        stringPower = 1#len(s) >= 1 as stated in the problem
        count = 1
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                count += 1
                if i + 1 == len(s) - 1:#reaching the end
                    if count > stringPower:
                        stringPower = count
            else:
                if count > stringPower:
                    stringPower = count
                count = 1
        return stringPower

    def maxPower_2(self, s: str) -> int:
        count = 0
        max_count = 0
        previous = None
        for c in s:
            if c == previous:
                count += 1
            else:
                previous = c
                count = 1
            max_count = max(max_count, count)
        return max_count