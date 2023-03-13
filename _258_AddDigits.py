class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            stNum = str(num)
            num = 0
            for l in stNum:
                num  = num + int(l)
            
        return num

    def addDigits_2(self, num: int) -> int:
        digit_root = 0
        while num > 0:
            digit_root += num % 10
            num = num // 10
            
            if num == 0 and digit_root > 9:
                num = digit_root
                digit_root = 0
        return digit_root