# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Runtime: 2496 ms, faster than 9.33% of Python3 online submissions for 
        #Insertion Sort List. Memory Usage: 16.3 MB, less than 68.48% of 
        #Python3 online submissions for Insertion Sort List.
        if not head or not head.next:
            return head
        A = []
        node = head
        while node:
            A.append(node)
            node = node.next
        for j in range(1, len(A)):
            tmp = A[j]
            i = j - 1
            while i >= 0 and A[i].val > tmp.val:
                A[i + 1] = A[i]
                i -= 1
            A[i + 1] = tmp
        for index in range(len(A) - 1):
            A[index].next = A[index + 1]
        A[-1].next = None
        return A[0]

    def insertionSortList_node(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Runtime: 188 ms, faster than 71.78% of Python3 online submissions for 
        #Insertion Sort List. Memory Usage: 16.5 MB, less than 30.28% of 
        #Python3 online submissions for Insertion Sort List.
        if not head or not head.next:
            return head
        
        dummyHead = ListNode(next=head)
        lastSorted = head
        cur = head.next
        while cur:
            if cur.val >= lastSorted.val:
                lastSorted = lastSorted.next
            else:
                prev = dummyHead
                while prev.next.val < cur.val:
                    prev = prev.next
                lastSorted.next = cur.next
                cur.next = prev.next
                prev.next = cur
            cur = lastSorted.next
        return dummyHead.next