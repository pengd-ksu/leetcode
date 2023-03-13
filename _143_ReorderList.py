# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList_list(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        
        nodeList = []
        node = head
        while node:
            nodeList.append(node)
            node = node.next
        left, right = 0, len(nodeList) - 1
        while left < right:#what if left == right?
            nodeList[left].next = nodeList[right]
            if left + 1 < right:
                nodeList[right].next = nodeList[left + 1]
            left += 1
            right -= 1
        nodeList[left].next = None#Now left is the last non-empty node
        return head

def reorderList_node(self, head):
    if not head or not head.next: return
    
    # Step 1: find the middle node
    middle = None
    slow, fast = head, head
    while fast and fast.next:
        middle = slow
        slow = slow.next
        fast = fast.next.next
    middle.next = None
    
    # Step 2: reverse the second half
    prev = None
    while slow:
        nextNode = slow.next
        slow.next = prev
        prev, slow = slow, nextNode
        
    # Step 3: merge two lists
    while head and prev:
        first, second = head.next, prev.next
        head.next = prev
        if first:
            prev.next = first
        head, prev = first, second