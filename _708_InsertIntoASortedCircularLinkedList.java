/*
// Definition for a Node.
class Node {
    public int val;
    public Node next;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _next) {
        val = _val;
        next = _next;
    }
};
*/

class Solution {
    public Node insert(Node head, int insertVal) {
        if (head == null) {
            Node node = new Node(insertVal);
            node.next = node;
            return node;
        }
        Node prev = head, curr = head.next;
        Node node = new Node(insertVal);
        while (true) {
            // Case 1. It's descending order, larger than prev,
            // smaller than curr
            if (insertVal >= prev.val &&
                insertVal <= curr.val) {
                prev.next = node;
                node.next = curr;
                return head;
            }
            // Case 2. Larger than all, or smaller than all, inserted
            // into between largest and smallest
            if (prev.val > curr.val) {
                if (insertVal <= curr.val || insertVal >= prev.val) {
                    prev.next = node;
                    node.next = curr;
                    return head;
                }
            }
            prev = curr;
            curr = curr.next;
            // Case 3. Loop all over but not in case 1 or 2.  
            // Therefore there're duplicate elements filled 
            // in the ring. Break the loop and inserted anywhere.
            if (prev == head) break;
        }
        node.next = curr;
        prev.next = node;
        return head;
    }
}