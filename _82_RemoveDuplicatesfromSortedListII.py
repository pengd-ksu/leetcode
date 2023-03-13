# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        node1 = head
        val_dic = {}
        while node1:
            val_dic[node1.val] = val_dic.get(node1.val, 0) + 1
            node1 = node1.next

        node2, keep = head, head
        flag_head, flag_first = True, True
        
        while node2:
            if val_dic[node2.val] == 1:
                if flag_first:
                    keep = node2
                    flag_first = False
                    if flag_head:
                        head = keep
                        flag_head = False
                else:
                    keep.next = node2
                    keep = keep.next
            node2 = node2.next
        if flag_head:
            return None
        else:
            keep.next = None#In case there's any following node in the head list
            return head

    def deleteDuplicates_sentinel(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(0, head)
        prev = sentinel
        
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next
            
        return sentinel.next

    def deleteDuplicates_recursive(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        if head.val == head.next.val:
            # skip duplicate nodes
            while head.next and head.val == head.next.val:
                head = head.next
            return self.deleteDuplicates_recursive(head.next)
        else:
            head.next = self.deleteDuplicates_recursive(head.next)
            return head