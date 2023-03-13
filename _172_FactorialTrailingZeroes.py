class Solution:
    def trailingZeroes(self, n: int) -> int:
        tmp = n
        sumZero = 0
        while tmp:
            tmp = tmp // 5
            sumZero += tmp
        return sumZero
    """
    Idea: A trailing 0 will be formed only if a number has both 2 and 5 as prime factors.
If there are x number of 2 and y number of 5 then number of trailing zeros is min(x,y)

Observation: Practically count of 2 >= count of 5 always. So we just need to find count of 5.

How to count 5: Since we are finding factorial of n, so we need to count the number of 5 in 1, 2 ,3 ,...,n. We can observe that after every five numbers a 5 occurs:
1, 2, 3, 4, 5 (5x1)
6, 7, 8, 9, 10 (5x2)
11, 12, 13, 14, 15 (5x3)
16, 17, 18, 19, 20 (5x2x2)
But numbers like 25, 125 (i.e 5^k) there will be extra 5s
25 (5x5)
125 (5x5x5)
...

So we need to count amount of numbers divisible by-
5 -> Containing one 5,
25 -> Containing two 5,
125 -> Containing three 5 ...
    """