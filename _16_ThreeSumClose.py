def threeSumClosest(self, nums: List[int], target: int) -> int:
    nums.sort()
    min_dif, final_three  = math.inf, math.inf
    
    for i in range(1, len(nums) - 1):
        l, r = 0, len(nums) - 1
     
        while l < i and i < r:
            three_sum = nums[l] + nums[i] + nums[r]
            new_dif = abs(three_sum - target)
            
            if new_dif < min_dif:
                final_three = three_sum
                min_dif = new_dif

            if three_sum < target:
                l += 1
            elif three_sum > target:
                r -= 1
            else:
                return target        
    
    return final_three