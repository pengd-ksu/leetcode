# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummyHead = ListNode()
        dummyHead.next = head
        node = dummyHead
        while head:
            if head.val == val:
                node.next = head.next
            else:
                node.next = head
                node = node.next
            head = head.next
        return dummyHead.next