# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        first = head
        second = head.next
        first.next = self.swapPairs(second.next)
        second.next = first
        return second


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # Dummy node acts as the prevNode for the head node
        # of the list and hence stores pointer to the head node.
        # Dummy node acts as the prevNode for the head node
        # of the list and hence stores pointer to the head node.
        dummy = ListNode(-1)
        dummy.next = head

        prev_node = dummy

        while head and head.next:

            # Nodes to be swapped
            first_node = head;
            second_node = head.next;

            # Swapping
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            # Reinitializing the head and prev_node for next swap
            prev_node = first_node
            head = first_node.next

        # Return the new head node.
        return dummy.next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        cur = head
        pre = head.next
        copy = pre
        
        while True:
            cur.next = pre.next
            pre.next = cur
            
            if cur.next is None or cur.next.next is None:
                break
            
            tmp = cur.next
            cur.next = tmp.next
            pre = tmp.next
            cur = tmp
            
        return copy