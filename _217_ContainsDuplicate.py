class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numSet = set()
        prev = 0
        for n in nums:
            numSet.add(n)
            cur = len(numSet)
            if cur == prev:
                return True
            prev = cur
        return False

    def containsDuplicate_2(self, nums: List[int]) -> bool:
        l1 = len(nums)
        l2 = len(set(nums))
        return not l1 == l2