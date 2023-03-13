# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST_brtue(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        if n >= 3:
            node = TreeNode(nums[n // 2])
            left = self.sortedArrayToBST(nums[:n // 2])
            right = self.sortedArrayToBST(nums[n//2 + 1:])
            node.left = left
            node.right = right
        elif n == 2:
            node = TreeNode(nums[n - 1])
            node.left = TreeNode(nums[0])
        elif n == 1:
            node = TreeNode(nums[n - 1])
        return node

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def BuildBST(l: int, r: int) -> Optional[TreeNode]:
            if l > r:
                return None
            mid = (l + r) // 2
            return TreeNode(nums[mid], BuildBST(l, mid - 1), BuildBST(mid + 1, r))
        return BuildBST(0, len(nums) - 1)