class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        @functools.lru_cache(None)
        def kmove(x, y, k):
            if x < 0 or x >= n or y < 0 or y >= n:
                return 0
            elif k == 0:
                return 1
            else:
                return (kmove(x + 2, y + 1, k - 1) +
                        kmove(x + 2, y - 1, k - 1) +
                        kmove(x + 1, y + 2, k - 1) +
                        kmove(x + 1, y - 2, k - 1) +
                        kmove(x - 2, y + 1, k - 1) +
                        kmove(x - 2, y - 1, k - 1) +
                        kmove(x - 1, y + 2, k - 1) +
                        kmove(x - 1, y - 2, k - 1)) / 8
        return kmove(row, column, k)