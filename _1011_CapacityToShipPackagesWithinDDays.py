class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(capacity):
            count = 1
            load = 0
            for w in weights:
                load += w
                if load > capacity:
                    count += 1
                    load = w
            if count > days:
                return False
            return True
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (right + left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = (left + right) // 2
            cnt = 1
            cur = 0
            for w in weights:
                cur += w
                if cur > mid:
                    cur = w
                    cnt += 1
            if cnt > days:
                left = mid + 1
            else:
                right = mid
        return left

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = (left + right) // 2
            cnt = 1
            cur = 0
            for w in weights:
                cur += w
                if cur > mid:
                    cur = w
                    cnt += 1
            if cnt > days:
                left = mid + 1
            else:
                right = mid
        return left