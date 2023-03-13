from typing import List

string = "ABC"
n = len(string)
a = list(string)

def permute(nums: List[int]) -> List[List[int]]:
    ans = []
    def permute_backtrack(num_list: List[int], l: int, r: int) -> None:
        if l == r:
            ans.append(list(num_list))#list to make a copy, otherwise when 
            #the function returns, the nums list will get back to originial 
            #due to backtrack
            return
        else:
            for i in range(l, r + 1):
                num_list[i], num_list[l] = num_list[l], num_list[i]
                permute_backtrack(num_list, l+1, r)
                num_list[i], num_list[l] = num_list[l], num_list[i]
                #backtrack to restore the list, so that next for loop will 
                #continue with the same list.
    permute_backtrack(nums, 0, len(nums)-1)
    return ans

    def permute_2(self, nums: List[int]) -> List[List[int]]:
        # Since the chosen one in each round will be removed from the choices for next couple rounds, there will be no duplicate. And each round (with fewer choices), there will be guaranteed to be a different number in this place since all the numbers in the array are distinct.
        ans = []
        
        def backtrack(path, nums, l, r): # r will be unreachable.
            if len(path) == len(nums): # We do not control nums, but its visible indices when being called.
                ans.append(list(path)) # list path to catch the elements (shallow copy), otherwise path will be changed in the function later. There are more than one call to the function backtrack.
                return
            for i in range(l, r):
                path.append(nums[i])
                nums[l], nums[i] = nums[i], nums[l] # Get the chosen one out of choices
                backtrack(path, nums, l + 1, r)
                path.pop() # Give it back, so another one will be in this place.
                nums[l], nums[i] = nums[i], nums[l] # swap them back
                
        backtrack([], nums, 0, len(nums))
        return ans

    def permute_dfs(self, nums: List[int]) -> List[List[int]]:
        def dfs(arr, path):
            if not arr:
                ans.append(path)
                return
            for i in range(len(arr)):
                dfs(arr[:i] + arr[i+1:], path + [arr[i]]) # Both 
                # arguments must be passed as a combination form, 
                # because these will be new arguments, no need to 
                # worry about their change later.
                
        ans = []
        dfs(nums, [])
        return ans

    def permute_recursive(self, nums: List[int]) -> List[List[int]]:
        return [[n] + p
               for i, n in enumerate(nums)
               for p in self.permute(nums[:i]+nums[i+1:]) or [[]]]
               # [[]] is the base case, when all the ele in nums has
               # been removed from choices of next round

    def permute_recursive2(self, nums: List[int]) -> List[List[int]]:
        # Insert the first number anywhere in any permutation of the remaining numbers.
        return nums and [p[:i] + [nums[0]] + p[i:]
                     for p in self.permute(nums[1:])
                     for i in range(len(nums))] or [[]]

    def permute_reduce(self, nums):
        # Use reduce to insert the next number anywhere in the already built permutations.
        return reduce(lambda P, n: [p[:i] + [n] + p[i:]
                                    for p in P for i in range(len(p)+1)],
                      nums, [[]])

if __name__ == '__main__':
    print(permute(a))