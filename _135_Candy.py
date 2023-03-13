class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        sumCandy = 0
        left2right = [1 for _ in range(n)]
        right2left = [1 for _ in range(n)]
        for i in range(n - 1):
            if ratings[i + 1] > ratings[i]:
                left2right[i + 1] = left2right[i] + 1
        for j in range(n - 1, 0, -1):
            if ratings[j - 1] > ratings[j]:
                right2left[j - 1] = right2left[j] + 1
        for index in range(n):
            sumCandy += max(left2right[index], right2left[index])
        return sumCandy

    def candy_brute(self, ratings: List[int]) -> int:
        #Can't pass due to time limit
        n = len(ratings)
        candies = [1 for _ in range(n)]
        hasChanged = True
        while hasChanged:
            hasChanged = False
            for i in range(n):
                if i != n - 1 and ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
                    candies[i] = candies[i + 1] + 1
                    hasChanged = True
                if i > 0 and ratings[i] > ratings[i - 1] and candies[i] <= candies[i - 1]:
                    candies[i] = candies[i - 1] + 1
                    hasChanged = True
        candySum = 0
        for candy in candies:
            candySum += candy
        return candySum

    def candy_oneArray(self, ratings: List[int]) -> int:
        n = len(ratings)
        sumCandy = 0
        candies = [1 for _ in range(n)]
        for i in range(n - 1):
            if ratings[i + 1] > ratings[i]:
                candies[i + 1] = candies[i] + 1#first loop, need to compare candies
        for j in range(n - 1, 0, -1):
            if ratings[j - 1] > ratings[j]:
                if candies[j - 1] <= candies[j]:
                    candies[j - 1] = candies[j] + 1
        for candy in candies:
            sumCandy += candy
        return sumCandy