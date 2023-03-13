# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle_1(self, head: Optional[ListNode]) -> bool:
        #If there's cycle in the link, a two step link will catch up with a 
        #step link finally
        if not head or not head.next or not head.next.next:
            return False
        node1, node2 = head.next, head.next.next
        while node1 and node2:
            if node1 is node2:
                return True
            if not node1.next:
                return False
            else:
                node1 = node1.next
            if (not node2.next) or (not node2.next.next):
                return False
            else:
                node2 = node2.next.next
        return False

    def hasCycle_2(self, head: Optional[ListNode]) -> bool:
        #Optimization from solution 1, fast is faster, so check it only is fine.
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                return True
        return False

    def hasCycle_3(self, head: Optional[ListNode]) -> bool:
        node = head
        while node:
            if node.val == 'seen':
                return True
            else:
                node.val = 'seen'
                node = node.next
        return False