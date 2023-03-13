# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0, None)
        head = ans
        while (l1 is not None) or (l2 is not None):
            if l1 is None:
                while l2 is not None:
                    ans.next = ListNode(l2.val)
                    l2 = l2.next
                    ans = ans.next
            elif l2 is None:
                while l1 is not None:
                    ans.next = ListNode(l1.val)
                    l1 = l1.next
                    ans = ans.next
            else:
                if l1.val < l2.val:
                    ans.next = ListNode(l1.val)
                    l1 = l1.next
                    ans = ans.next
                else:
                    ans.next = ListNode(l2.val)
                    l2 = l2.next
                    ans = ans.next
                
        return head.next

    def mergeTwoLists_2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0, None)
        head = ans
        while (l1 is not None) and (l2 is not None):
            if l1.val <= l2.val:
                ans.next = ListNode(l1.val)
                l1 = l1.next
                ans = ans.next
            else:
                ans.next = ListNode(l2.val)
                l2 = l2.next
                ans = ans.next
        if l1 is not None:
            ans.next = l1
        elif l2 is not None:
            ans.next = l2

        return head.next

    def mergeTwoLists_3(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        node = head
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
                node = node.next
            else:
                node.next = l2
                l2 = l2.next
                node = node.next
        if l1:
            node.next = l1#Draw a picture, will understand why it's node.next
        elif l2:
            node.next = l2
        return head.next

    def mergeTwoLists_4(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2