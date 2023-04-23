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
        List<Integer> vals = new ArrayList<>();
        ListNode node = head;
        while(node != null) {
            vals.add(node.val);
            node = node.next;
        }
        int l = 0, r = vals.size() - 1;
        while (l < r) {
            if (vals.get(l) != vals.get(r)) {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
}