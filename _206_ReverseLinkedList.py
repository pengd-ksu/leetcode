# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode()
        while head:
            if head.next:
                tmp = head.next
                head.next = dummyHead.next
                dummyHead.next = head
                head = tmp
            else:#head is the last but None node.
                head.next = dummyHead.next
                dummyHead.next = head
                head = None
        return dummyHead.next