/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        if (head == null) {
            return null;
        }
        Node node = head;
        HashMap<Node, Node> mp = new HashMap<>();
        while (node != null) {
            Node cp = new Node(node.val);
            mp.put(node, cp);
            node = node.next;
        }
        node = head;
        while (node != null) {
            mp.get(node).next = mp.get(node.next);
            mp.get(node).random = mp.get(node.random);
            node = node.next;
        }
        return mp.get(head);
    }
}