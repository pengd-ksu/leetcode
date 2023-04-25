# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or not k:
            return head#in case there's only one node/null, or k equals 0
        
        def list_len(a_head):
            n = 0
            if not a_head:
                pass
            else:
                while a_head:
                    a_head = a_head.next
                    n += 1
            return n
        
        def rotate_once(head_node):
            if not head_node:
                return head_node#null node
            new_head = None
            original_head = head_node
            while head_node.next.next:
                head_node = head_node.next
            new_head = head_node.next
            head_node.next = None
            new_head.next = original_head
            return new_head
        
        length = list_len(head)
        if length != 0:
            rotation = k % length
        else:
            rotation = k
        
        for _ in range(rotation):
            head = rotate_once(head)
            
        return head
        