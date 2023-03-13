# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #not head must be first, because head could be null. And or won't check
        #later sequence as long as there's True in the previous ones.
        if not head or head.next == None:
            return head
        prev = head
        node = head.next
        while node:
            if node.val == prev.val:
                prev.next = node.next
                node = node.next
            else:
                prev = node
                node = node.next
        return head