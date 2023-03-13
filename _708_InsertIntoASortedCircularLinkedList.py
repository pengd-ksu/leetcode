"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution: # Official approach
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if head == None:
            node = Node(insertVal, None)
            node.next = node
            return node
        
        prev, cur = head, head.next
        toInsert = False
        while True:# how to end?
            if prev.val <= insertVal <= cur.val:#Among the largest and smallest
                toInsert = True
            elif prev.val > cur.val:# It is the largest or smallest
                if insertVal < cur.val or insertVal > prev.val:
                    toInsert = True
            if toInsert:
                prev.next = Node(insertVal, cur)
                return head
            prev, cur = cur, cur.next
            # Only one node
            if prev == head:
                break
        
        prev.next = Node(insertVal, cur)
        return head

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if head == None:
            node = Node(insertVal, None)
            node.next = node
            return node
        
        prev, cur = head, head.next
        while True:
            if prev.val <= insertVal <= cur.val:
                node = Node(insertVal, cur)
                prev.next = node
                return head
            elif prev.val > cur.val:
                if insertVal < cur.val or insertVal > prev.val:
                    node = Node(insertVal, cur)
                    prev.next = node
                    return head
        # It's possible that sorted list can contain some duplicate values
            prev, cur = cur, cur.next#One loop over, couldn't insert
            if prev == head:
                break

        prev.next = Node(insertVal, cur)
        return head