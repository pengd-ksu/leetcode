/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        // Let fast: 2n, and slow: n, go from start of the sequence,
        // and they should meet some place in the cycle. At that point,
        // we have 2n-n = n == k*p, p is the perimeter of the cycle. And
        // k is an integer. Suppose i is the first index in the cycle. 
        // Then we should have x[i+kp] = x[i], since kp is the repetition 
        // of the cycle. So we know that, once we got x[kp], we let slow 
        // go from start, the other slow go from the point where fast and 
        // slow met, we should have x[i+kp] = x[i]. And we will find i.
        if (head == null || head.next == null) {
            return null;
        }
        ListNode slow = head.next;
        ListNode fast = head.next.next;
        ListNode start = null;
        while (fast != null && fast.next != null) {
            if (fast == slow) {
                start = fast;
                break;
            }
            slow = slow.next;
            fast = fast.next.next;
        }
        if (start == null) {
            return null;
        }
        ListNode res = head;
        while (res != start) {
            res = res.next;
            start = start.next;
        }
        return res;
    }
}