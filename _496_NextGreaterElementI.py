class Solution: # Similar to approach 1
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for n1 in nums1:
            ans = None
            for i in range(len(nums2) - 1, -1, -1):
                if nums2[i] == n1:
                    break
                elif nums2[i] > n1:
                    ans = nums2[i]
            if ans == None:
                result.append(-1)
            else:
                result.append(ans)
        return result

class Solution: # Approach 2 Python version
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map = dict()
        stack = []
        result = []
        
        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                map[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        
        while stack:
            map[stack.pop()] = -1
            
        for j in range(len(nums1)):
            result.append(map[nums1[j]])
            
        return result