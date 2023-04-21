/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        // Key observation: if there's an intersection, the last parts of headA
        // and headB must be same, like this:
        // A: xxxYYYYY
        // B:  ooYYYYY
        // It means we should have a sequnce of equal lists. In the solution,
        // we made a as the longer list. But remember to check boundary, since
        // node.next might invoke null pointer.
        int lenA = 0;
        int lenB = 0;
        ListNode a = headA;
        ListNode b = headB;
        while (a != null) {
            lenA += 1;
            a = a.next;
        }
        while (b != null) {
            lenB += 1;
            b = b.next;
        }
        if (lenA > lenB) {
            a = headA;
            b = headB;
        } else {
            a = headB;
            b = headA;
        }
        // Always check if null since .next might invoke null pointer
        for (int i = 0; i < Math.abs(lenA - lenB) && a != null; i++) {
            a = a.next;
        }
        // Always check if null since .next might invoke null pointer
        while (a != b && a != null && b != null) {
            a = a.next;
            b = b.next;
        }
        return a;
    }
}