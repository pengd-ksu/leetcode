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
        HashSet<ListNode> s = new HashSet<>();
        ListNode a = headA;
        ListNode b = headB;
        while (a != null) {
            s.add(a);
            a = a.next;
        }
        while(b != null) {
            if (s.contains(b)) {
                return b;
            }
            s.add(b);
            b = b.next;
        }
        return null;
    }
}