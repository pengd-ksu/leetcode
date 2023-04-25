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
    public ListNode rotateRight(ListNode head, int k) {
        // Case 1. len will be 0
        if (head == null) return head;
        int len = 1;
        ListNode prevTail = head;
        while (prevTail.next != null) {
            prevTail = prevTail.next;
            len++;
        }
        k = k % len;
        // Case 2. No rotation.
        if (k == 0) return head;
        ListNode newTail = head;
        int move = len - k;

        while (move > 1) {
            newTail = newTail.next;
            move--;
        }
        ListNode newHead = newTail.next;
        newTail.next = null;
        prevTail.next = head;
        return newHead;
    }
}