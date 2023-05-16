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
        ListNode front = null, back = null, curr = head;
        int len = 0;
        while (curr != null) {
            len++;
            if (back != null) {
                back = back.next;
            }
            if (len == k) {
                front = curr;
                back = head;
            }
            curr = curr.next;
        }
        int tmp = front.val;
        front.val = back.val;
        back.val = tmp;
        return head;
    }
}