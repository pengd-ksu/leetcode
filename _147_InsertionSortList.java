/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode insertionSortList(ListNode head) {
        ListNode curr = head;
        ListNode dummy = new ListNode();

        // We save all kinds of trouble with prev and next by a reordered
        // linkedlist
        while (curr != null) {
            ListNode prev = dummy;
            while (prev.next != null && prev.next.val <= curr.val) {
                prev = prev.next;
            }
            ListNode nxt = curr.next;
            curr.next = prev.next;
            prev.next = curr;
            curr = nxt;
        }

        return dummy.next;
    }
}