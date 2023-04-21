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
    public ListNode removeElements(ListNode head, int val) {
        ListNode prev;
        ListNode curr;
        ListNode newHead = head;

        while (newHead != null) {
            if (newHead.val != val) {
                break;
            }
            newHead = newHead.next;
        }
        if (newHead == null) {
            return newHead;
        }
        prev = curr = newHead;

        while (curr != null) {
            if (curr.val != val) {
                prev = curr;
                curr = curr.next;
            } else {
                prev.next = curr.next;
                curr = curr.next;
            }
        }
        return newHead;
    }
}