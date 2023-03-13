# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return head
        if not head.next:
            return TreeNode(head.val)
        slow, fast = head, head.next.next#fast go earlier, because need to cut
        #off slow.next later, as well as to track root
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        root = TreeNode(slow.next.val)
        right = slow.next.next
        slow.next = None
        left = head
        root.left = self.sortedListToBST(left)
        root.right = self.sortedListToBST(right)
        return root