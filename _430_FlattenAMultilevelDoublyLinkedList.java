/*
// Definition for a Node.
class Node {
    public int val;
    public Node prev;
    public Node next;
    public Node child;
};
*/

class Solution {
    public Node flatten(Node head) {
        // Base case, when reaching the end. The caller need to check
        // against null pointer caused by null calling prev or next.
        if (head == null) return head;
        Node n = head;
        while (n != null) {
            if (n.child == null) {
                n = n.next;
            } else {
                // nxt is to the right, result could be null
                Node nxt = flatten(n.next);
                // sub is to the child, result definitely won't be null
                Node sub = flatten(n.child);
                // eliminate child since returned list should be flat
                n.child = null;
                n.next = sub;
                sub.prev = n;
                // Get to the end of the newly inserted part, and 
                // establish prev and next connection with the rest
                // of the list
                // Rember that sub won't be null since it's child
                while (sub.next != null) {
                    sub = sub.next;
                }
                if (nxt != null) {
                    sub.next = nxt;
                    nxt.prev = sub;
                }
                // In this case, break the while, since rest of the work
                // will be caught on by recursion on the right and child
                // side
                break;
            }
        }
        return head;
    }
}