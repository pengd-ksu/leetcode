# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        node = head
        while node:
            if node.val == 'seen':
                return node
            else:
                node.val = 'seen'
                node = node.next
    
    def detectCycle_floyd(self, head: ListNode) -> ListNode:
        if not head:
            return None

        fast, slow = head, head
        isCycle = False

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                isCycle = True
                break

        if not isCycle:
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
#https://en.wikipedia.org/wiki/Cycle_detection#cite_note-knuth-3 for floyed method