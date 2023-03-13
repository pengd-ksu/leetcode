class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        start = 0
        for n in nums:
            start ^= n
        return start

    def singleNumber_2(self, nums: List[int]) -> int:
        dic = {}
        for n in nums:
            dic[n] = dic.get(n, 0) + 1
        for key, val in dic.items():
            if val == 1:
                return key

    def singleNumber_3(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x^y, nums)

    def singleNumber_4(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)

    def singleNumber_5(self, nums: List[int]) -> int:
        return reduce(operator.xor, nums)