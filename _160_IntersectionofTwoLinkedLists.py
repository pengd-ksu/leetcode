# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a, b = headA, headB
        nodeSet = set()
        flag = True
        while a or b:
            if a:
                if a not in nodeSet:
                    nodeSet.add(a)
                    a = a.next
                else:
                    return a
            if b:
                if b not in nodeSet:
                    nodeSet.add(b)
                    b = b.next
                else:
                    return b
        return None

    def getIntersectionNode_ConstantMemo(self, headA: ListNode, headB: ListNode) -> ListNode:
        #key insight: 1. if the two have intersections, their last nodes must be the same
        #2. If they are intersected, cut them to the same length from the beginning, the remaining parts of both must contain the intersection 
        sizeA = sizeB = 0
        nodeA = headA
        lastA = None
        while nodeA:
            if nodeA.next is None:
                lastA = nodeA
            sizeA += 1
            nodeA = nodeA.next
        
        nodeB = headB
        lastB = None
        while nodeB:
            if nodeB.next is None:
                lastB = nodeB
            sizeB += 1
            nodeB = nodeB.next
        
        if nodeA is not nodeB:
            return None
        
        nodeA, nodeB = headA, headB
        if sizeA > sizeB:
            for _ in range(sizeA - sizeB):
                nodeA = nodeA.next
        elif sizeA < sizeB:
            for _ in range(sizeB - sizeA):
                nodeB = nodeB.next
        
        while nodeA and nodeB:
            if nodeA is nodeB:
                return nodeA
            nodeA = nodeA.next
            nodeB = nodeB.next