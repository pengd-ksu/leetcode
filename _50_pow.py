class Solution:
    def myPow_recur(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            return self.myPow_recur(1/x, -n)
        else:
            if n % 2 == 0:
                return self.myPow_recur(x ** 2, n // 2)
            else:
                return x * self.myPow_recur(x, n - 1)

    def myPow_iter(x: float, n: int) -> float:
        def iter(x, absn, result):
            if absn == 0:
                return result
            else:
                if absn % 2 == 0:
                    return iter(x ** 2, absn // 2, result)
                else:
                    return iter(x, absn - 1, x * result)
        if n < 0:
            return iter(1/x, abs(n), 1)
        else:
            return iter(x, n, 1)

if __name__ == '__main__':
    print(Solution.myPow_iter(2.0, 10))