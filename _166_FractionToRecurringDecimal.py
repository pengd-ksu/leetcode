from typing import List

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        #It's only based on very simple repetition, can't handle pattern like
        #1.414, because 4 appears more than once.
        if numerator * denominator < 0:
            sign = '-'
            numerator, denominator = abs(numerator), abs(denominator)
        else:
            sign = ''
        q, r = divmod(numerator, denominator)
        if r == 0:
            return sign + str(q)
        s = str(q) + '.'
        remainDict = dict()
        frac = ''
        while r:
            #already seen remains, break; else, continue
            if r in remainDict:
                l = remainDict[r]
                frac = frac[:l] +'(' + frac[l:] + ')'
                break
            remainDict[r] = len(frac)
            r *= 10
            q, r = divmod(r, denominator)
            frac += str(q)
        return sign + s + frac