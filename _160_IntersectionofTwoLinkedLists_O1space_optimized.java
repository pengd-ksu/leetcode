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
        // Suppose headA and headB are intersected, then they must share
        // the same tail. Suppose the shared tail is c, and exclusive part
        // for headA is a, exclusive part for headB is b, since 
        // a+c+b == b+c+a, we will have a key finding: headA travels until
        // tail null and continues with exclusive part headB(b), will get 
        // to the same point that started from headB till end and continueed
        // with exclusive part of headA. Even if they didn't intersect, 
        // since the travelling length will be the same, both of the will 
        // reach the end null after the same iteration. Safe to have a 
        // while test.
        ListNode a = headA;
        ListNode b = headB;
        while (a != b) {
            a = a == null ? headB : a.next;
            b = b == null ? headA : b.next;
        }
        return a;
    }
}