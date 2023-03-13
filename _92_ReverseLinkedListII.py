from typing import List

from pytest import mark

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return head
        
        left_pointer, right_pointer = head, head
        stop = False
        
        def recurseAndReverse(right: ListNode, m: int, n: int) -> None:
            if n == 1:
                return
            nonlocal left_pointer, stop
            right = right.next
            if m > 1:
                left_pointer = left_pointer.next
            recurseAndReverse(right, m - 1, n - 1)
            if right.next == left_pointer or left_pointer == right:
                stop = True
            if not stop:
                left_pointer.val, right.val = right.val, left_pointer.val
                left_pointer = left_pointer.next
                
        recurseAndReverse(right_pointer, left, right)
        return head

    def reverseBetween_recursive(self, head, m, n):
        # Empty list
        if not head:
            return head
        #First reverse the list, then fix the connections
        cur, prev = head, None
        while left > 1:
            prev = cur
            cur = cur.next
            left, right = left - 1, right - 1
        
        con, tail = prev, cur
        
        while right:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            right -= 1
        
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur
        return head