# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node = head
        nodeList = []
        while node:
            nodeList.append(node.val)
            node = node.next
        return nodeList[::-1] == nodeList

    def isPalindrome_2(self, head: Optional[ListNode]) -> bool:
        #compare the fist half with the second half while reversing first half
        slow, fast = head, head
        rev = None
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:#the node has odd numbers
            slow = slow.next
        while rev and rev.val == slow.val:
            rev, slow = rev.next, slow.next
        return not rev

    def isPalindrome_3(self, head: Optional[ListNode]) -> bool:
        #reverse the first half list back
        slow, fast = head, head
        rev = None
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        tail = slow.next if fast else slow
        while rev and rev.val == tail.val:
            slow, slow.next, rev = rev, slow, rev.next
            tail = tail.next
        return not rev