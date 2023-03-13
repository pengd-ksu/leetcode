# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #complementation. cut copy2 into 2 parts, n from the beginning, and the rest. The copy1 move the length of second part, it will have n distance from the end
        copy1, copy2 = head, head
        while n:
            copy2 = copy2.next
            n -= 1
        if not copy2:
            return head.next
            
        while copy2.next:
            copy1 = copy1.next
            copy2 = copy2.next
        copy1.next = copy1.next.next
        
        return head