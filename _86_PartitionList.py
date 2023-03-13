# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        before, after = None, None
        while head:
            tmp = head.next#preserver next node in order
            head.next = None#cut off the previous link
            if head.val < x:
                if before != None:
                    before.next = head
                    before = before.next
                else:#initial before sequence
                    before = head
                    before_first = before
            else:
                if after != None:
                    after.next = head
                    after = after.next
                else:#initial after sequence
                    after = head
                    after_first = after
            head = tmp
        if before == None:
            return after_first
        if after == None:
            return before_first
        before.next = after_first
        return before_first
#before is the last pointer of a sequence that each contains val < x, could 
#be null, and before_first keeps the first pointer in the sequence
#after is the last pointer of a sequence that each contains val >= x, could 
#be null of course. And after_first keeps the first pointer in the sequence