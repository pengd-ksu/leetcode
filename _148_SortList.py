# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        def mergeSort(arr):
            if len(arr) > 1:
                mid = len(arr) // 2
                L = arr[:mid]
                R = arr[mid:]
                mergeSort(L)
                mergeSort(R)
                i = j = k = 0
                while i < len(L) and j < len(R):
                    if L[i].val < R[j].val:#.val method for the node
                        arr[k] = L[i]
                        i += 1
                    else:
                        arr[k] = R[j]
                        j += 1
                    k += 1
                while i < len(L):#only one of this would be possible if at all
                    arr[k] = L[i]
                    i += 1
                    k += 1
                while j < len(R):
                    arr[k] = R[j]
                    j += 1
                    k += 1
        
        nodeList = []
        node = head
        while node:
            nodeList.append(node)
            node = node.next

        mergeSort(nodeList)
        for index in range(len(nodeList) - 1):
            nodeList[index].next = nodeList[index + 1]
        nodeList[-1].next = None
        return nodeList[0]


    def sortList_node(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def getMid(head):
            midPrev = None
            while head != None and head.next != None:
                midPrev = head if midPrev == None else midPrev.next
                head = head.next.next
            mid = midPrev.next
            midPrev.next = None#Cut the linked list into two halves
            return mid
        def merge(list1, list2):
            dummyHead = ListNode()
            tail = dummyHead
            while list1 and list2:
                if list1.val < list2.val:
                    tail.next = list1
                    list1 = list1.next
                    tail = tail.next
                else:
                    tail.next = list2
                    list2 = list2.next
                    tail = tail.next
            tail.next = list1 if list1 else list2
            return dummyHead.next
        
        if not head or not head.next:
            return head
        mid = getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return merge(left, right)