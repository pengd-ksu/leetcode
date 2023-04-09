public class ListNode {
    int val;
    ListNode next;
    ListNode (int x) {
        val = x;
    }
}

class MyLinkedList {
    int size;
    ListNode head;

    public MyLinkedList() {
        size = 0;
        head = new ListNode(0);
    }
    
    public int get(int index) {
        if (index < 0 || index >= size) {
            return -1;
        }
        ListNode curr = head;
        for (int i = 0; i < index + 1; i++) {
            curr = curr.next;
        }
        return curr.val;
    }
    
    public void addAtHead(int val) {
        addAtIndex(0, val);
    }
    
    public void addAtTail(int val) {
        addAtIndex(size, val);
    }
    
    public void addAtIndex(int index, int val) {
        if (index > size || index < 0) {
            return;
        }
        ListNode prev = head;
        ListNode node = new ListNode(val);
        while (index > 0) {
            index -= 1;
            prev = prev.next;
        }
        node.next = prev.next;
        prev.next = node;
        size += 1;
    }
    
    public void deleteAtIndex(int index) {
        if (index >= size || index < 0) {
            return;
        }
        ListNode prev = head;
        while (index > 0) {
            index -= 1;
            prev = prev.next;
        }
        prev.next = prev.next.next;
        size -= 1;
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */