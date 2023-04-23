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
 /*
    An example was given by editor to show recursive way of printing
    elements in reverse order:
    function print_values_in_reverse(ListNode head)
        if head is NOT null
            print_values_in_reverse(head.next)
            print head.val
 */
class Solution {
    private ListNode frontPointer;

    public boolean isPalindrome(ListNode head) {
        frontPointer = head;
        return recursiveCheck(head);
    }

    // Because the program stablished a stack frame for each call,
    // in fact the space complexity is o(n)
    public boolean recursiveCheck(ListNode curr) {
        if (curr != null) {
            if (!recursiveCheck(curr.next)) return false;
            if (curr.val != frontPointer.val) return false;
            frontPointer = frontPointer.next;
        }
        return true;
    }
}