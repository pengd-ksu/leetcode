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
                n.child = null;
                n.next = sub;
                sub.prev = n;
                while (sub.next != null) {
                    sub = sub.next;
                }
                if (nxt != null) {
                    sub.next = nxt;
                    nxt.prev = sub;
                }
                break;
            }
        }
        return head;
    }
}