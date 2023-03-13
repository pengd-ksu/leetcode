class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        ans = ''
        for i, v in enumerate(values):
            ans += (num // v) * numerals[i]
            num = num % v
        return ans

    def intToRoman_2(self, num: int) -> str:
        valRoman = {1000: 'M', 900: 'CM', 500: 'D', 400:'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9:'IX', 5: 'V', 4: 'IV', 1: 'I'}
        ans = ''
        for key in valRoman.keys():
            ans += num // key * valRoman[key]
            num %= key
        return ans
