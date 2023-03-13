class Solution:
    def countPrimes_brute(self, n: int) -> int:#O(n^1.5), Time Limit Exceeded
        def isPrime(num: int):
            if num <= 1:
                return False
            for i in range(2, int(math.sqrt(num) + 1)):
                if num % i == 0:
                    return False
            return True
        count = 0
        for i in range(1, n):
            if isPrime(i):
                count += 1
        return count

    def countPrimes_Eratosthenes(self, n: int) -> int:
        isPrime = [True] * n
        for i in range(2, int(sqrt(n)) + 1):
            if not isPrime[i]:
                continue
            for j in range(i**2, n, i):
                isPrime[j] = False
        count = 0
        for i in range(2, n):
            if isPrime[i]:
                count += 1
        return count