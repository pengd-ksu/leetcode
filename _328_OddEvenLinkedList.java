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
    public ListNode oddEvenList(ListNode head) {
        if (head == null || head.next == null || head.next.next == null) {
            return head;
        }
        
        ListNode odd = head;
        ListNode node = head.next.next;
        ListNode even = head.next;
        ListNode h2 = even;
        int i = 3;

        while (node != null) {
            if (i % 2 != 0) {
                odd.next = node;
                odd = odd.next;
            } else {
                even.next = node;
                even = even.next;
            }
            i++;
            node = node.next;
        }
        odd.next = h2;
        even.next = null;
        return head;
    }
}