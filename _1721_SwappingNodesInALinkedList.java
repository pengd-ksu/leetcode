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
    public ListNode swapNodes(ListNode head, int k) {
        // 1 <= k <= n <= 10^5, no need for corner case
        int len = 0;
        ListNode curr = head;
        while (curr != null) {
            len++;
            curr = curr.next;
        }
        ListNode front = head;
        for (int i = 1; i < k; i++) {
            front = front.next;
        }
        ListNode back = head;
        // Since k <= n, we don't need module
        for (int i = 1; i <= len - k; i++) {
            back = back.next;
        }
        int tmp = front.val;
        front.val = back.val;
        back.val = tmp;
        return head;
    }
}