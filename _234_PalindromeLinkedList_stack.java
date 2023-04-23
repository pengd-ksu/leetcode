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
    public boolean isPalindrome(ListNode head) {
        int l = 0;
        ListNode n1 = head, n2 = head;
        Stack<Integer> s = new Stack<>();
        // Dummy ele in case there's only one 
        s.push(0);
        while (n1 != null) {
            l++;
            n1 = n1.next;
        }
        for (int i = 0; i < l; i++) {
            if (i < l/2) {
                s.push(n2.val);
            } else if (i == l/2 && l % 2 != 0) {
                ;
            } else {
                if (n2.val != s.pop()) {
                    return false;
                }
            }
            n2 = n2.next;
        }
        return true;
    }
}