# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next
        nodes.sort()
        head = ListNode(0)
        ans = head
        for node in nodes:
            ans.next = ListNode(node)
            ans = ans.next
            
        return head.next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l, r):
            if not l or not r:
                return l or r
            if l.val < r.val:
                l.next = merge(l.next, r)
                return l
            else:
                r.next = merge(l, r.next)
                return r
        
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = (len(lists)) // 2
        l, r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        return merge(l, r)