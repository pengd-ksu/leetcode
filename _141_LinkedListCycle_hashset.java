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
    public boolean hasCycle(ListNode head) {
        HashSet<ListNode> ns = new HashSet<>();
        ns.add(head);// this line could be omitted
        while (head != null) {
            if (ns.contains(head.next)) {
                return true;
            }
            ns.add(head.next);
            head = head.next;
        }
        return false;
    }
}