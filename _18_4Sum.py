from typing import List

def fourSum(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()

    if len(nums) < 4:
        return []

    ans = []
    check = set()

    for i in range(len(nums) - 3):

        three_sum = target - nums[i]

        for j in range(i + 2, len(nums) - 1):
            l, r = i + 1, len(nums) - 1
            while l < j and j < r:
                if nums[l] + nums[j] + nums[r] == three_sum:
                    if str([nums[i], nums[l], nums[j], nums[r]]) not in check:
                        ans.append([nums[i], nums[l], nums[j], nums[r]])
                        check.add(str([nums[i], nums[l], nums[j], nums[r]]))
                    l, r = l + 1, r - 1
                elif nums[l] + nums[j] + nums[r] < three_sum:
                    l += 1
                else:
                    r -= 1

    return ans

if __name__ == '__main__':
    print(fourSum([1,0,-1,0,-2,2], 0))