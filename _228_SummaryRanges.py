class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 1:
            return [str(nums[0])]
        elif len(nums) == 0:
            return []
        res = []
        ans = ''
        for i in range(len(nums) - 1):
            if nums[i] != nums[i+1] - 1:
                if not ans:
                    ans = str(nums[i])
                    res.append(ans)
                else:
                    if ans[-1] == '>':
                        ans += str(nums[i])
                        res.append(ans)
                    else:
                        res.append(ans)
                ans = str(nums[i+1])
            else:
                if not ans:
                    ans = str(nums[i]) +'->'
                else:
                    if ans[-1] == '>':
                        continue
                    else:
                        ans += '->'
                        #ans = str(nums[i]) +'->'
        if ans[-1] == '>':
            ans += str(nums[-1])
            res.append(ans)
        else:
            if res[-1] != ans:
                res.append(ans)
        return res

    def summaryRanges_2(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        res = []
        nums = nums + [nums[-1] + 100]
        #To handle situation when nums is continuous, such as [1, 2, 3, 4], the dummy end would be different from the last one 
        head = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 1:
                if head == nums[i-1]:
                    res.append(str(head))
                else:
                    res.append(str(head) + '->' + str(nums[i-1]))
                head = nums[i]
        return res