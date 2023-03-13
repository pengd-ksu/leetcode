class Solution:
    def numberToWords(self, num: int) -> str:
        def one(n):
            switcher = {
                1: 'One',
                2: 'Two',
                3: 'Three',
                4: 'Four',
                5: 'Five',
                6: 'Six',
                7: 'Seven',
                8: 'Eight',
                9: 'Nine'
            }
            return switcher.get(n)
        
        def two_less_20(n):
            switcher = {
                10: 'Ten',
                11: 'Eleven',
                12: 'Twelve',
                13: 'Thirteen',
                14: 'Fourteen',
                15: 'Fifteen',
                16: 'Sixteen',
                17: 'Seventeen',
                18: 'Eighteen',
                19: 'Nineteen'
            }
            return switcher.get(n)
        
        def ten(n):
            switcher = {
                2: 'Twenty',
                3: 'Thirty',
                4: 'Forty',
                5: 'Fifty',
                6: 'Sixty',
                7: 'Seventy',
                8: 'Eighty',
                9: 'Ninety'
            }
            return switcher.get(n)
        
        def two(n):
            if not n:
                return ''
            elif n < 10:
                return one(n)
            elif n < 20:
                return two_less_20(n)
            else:
                tenner = n // 10
                rest = n - tenner * 10
                return ten(tenner) + ' ' + one(rest) if rest else ten(tenner)
        
        def three(n):
            hundred = n // 100
            rest = n - hundred * 100
            if hundred and rest:
                return one(hundred) + ' Hundred ' + two(rest)
            elif not hundred and rest:
                return two(rest)
            elif hundred and not rest:
                return one(hundred) + ' Hundred'
        
        billion = num // 1000000000
        million = (num - billion * 1000000000) // 1000000
        thousand = (num - billion * 1000000000 - million * 1000000) // 1000
        rest = num - billion * 1000000000 - million * 1000000 - thousand * 1000
        
        if not num:
            return 'Zero'
        
        result = ''
        if billion:
            result = three(billion) + ' Billion'
        if million:
            result += ' ' if result else ''
            result += three(million) + ' Million'
        if thousand:
            result += ' ' if result else ''
            result += three(thousand) + ' Thousand'
        if rest:
            result += ' ' if result else ''
            result += three(rest)
        return result