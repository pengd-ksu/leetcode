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
        if (head == null) return head;
        int len = 0;
        ListNode node = head;
        while (node != null) {
            node = node.next;
            len++;
        }
        k = k % len;
        if (k == 0) return head;
        node = head;
        int move = len - k;
        ListNode prev = null;
        while (move > 0) {
            prev = node;
            node = node.next;
            move--;
        }
        ListNode newHead = node;
        prev.next = null;
        // Check for node == null is covered by k == 0
        while (node.next != null) {
            node = node.next;
        }
        node.next = head;
        return newHead;
    }
}