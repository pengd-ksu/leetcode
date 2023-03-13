class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        movingBits = 0
        while left != right:
            left >>= 1
            right >>= 1
            movingBits += 1
        return left << movingBits
    #Get inspiration from vic_Tim's answer in https://leetcode.com/problems/
    #bitwise-and-of-numbers-range/discuss/56729/Bit-operation-solution(JAVA)
    #for number 26 to 30: 11010, 11011, 11100, 11101, 11110, will only keep 
    #the common leading 1 prefix of 26 (smallest number, 11010) and 30 
    #(largest number, 11110), which is 11000. What if left and right have 
    #different number of bits? Try 1 and 3, the result is zero which is 
    #still correct.