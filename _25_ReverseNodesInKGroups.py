# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    #https://leetcode.com/problems/reverse-nodes-in-k-group/discuss/718457/python3-easy-recursion-solution
        cur = head
        for _ in range(k):
            if not cur:# The last part doesn't have k nodes
                return head
            cur = cur.next
        prev = None
        cur = head
        
        for _ in range(k):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        # head is the tail now! And cur is the head of next section.
        head.next = self.reverseKGroup(cur, k)
        # prev is the head of the first section of the nodes now!
        return prev

    def reverseKGroup_peng(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1 or not head:
            return head
        
        ans, copy, first, tail = head, head, head, head
        index = 0
        head_count = 0
        
        while copy:
            if index == 0:
                pre_tail = tail
                tail = copy
            
            copy = copy.next
            index += 1

            if index == k:
                tmp1 = first.next
                first.next = copy
                while index > 1:
                    tmp2 = tmp1.next
                    tmp1.next = first
                    first = tmp1
                    tmp1 = tmp2
                    index -= 1
                    
                head_first = first
                head_count += 1
                if head_count > 1:
                    pre_tail.next = first
                if head_count == 1:
                    ans = head_first
                    
                first = copy
                index = 0
            
        return ans