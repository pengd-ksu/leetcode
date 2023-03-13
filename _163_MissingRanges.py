class Solution: # Memory Limit Exceeded for case: [1000000000], 0, 1000000000
    # I think whole contains too many elements
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        check = set(nums)
        whole = [i for i in range(lower, upper + 1)]
        ans = [i for i in whole if i not in check]
        if len(ans) == 1:
            return [str(ans[0])]
        if len(ans) == 0:
            return []
        res = []
        idx = 0
        end = None
        while idx < len(ans) - 1: # Can't handle discrete elements in the last part
            # nor length of ans as 1
            if ans[idx+1] - ans[idx] == 1:
                start = ans[idx]
                idx += 1
                while idx < len(ans) - 1 and ans[idx+1] - ans[idx] == 1:
                    idx += 1
                end = ans[idx]
                res.append(str(start) + '->' + str(end))

            else:
                res.append(str(ans[idx]))
            idx += 1
        if ans[-2] != ans[-1] - 1: # Can't handle empty
            res.append(str(ans[-1]))
        return res

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        def formatRange(lower, upper):
            if lower == upper:
                return str(lower)
            elif lower < upper:
                return str(lower) + '->' + str(upper)
            
        result = []
        prev = lower - 1#Edge case one, start from lower
        for i in range(len(nums) + 1):
            # Edge case 2: check if upper is already in the range.
            cur = nums[i] if i < len(nums) else upper + 1
            if prev + 1 <= cur - 1:
                result.append(formatRange(prev + 1, cur - 1))
            prev = cur
        return result