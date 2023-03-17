class Node {
    public int value;
    public Node next;

    public Node (int value) {
        this.value = value;
        this.next = null;
    }
}

class MyCircularQueue {
    private Node head, tail;
    private int capacity;
    private int count;

    public MyCircularQueue(int k) {
        this.capacity = k;
    }
    
    public boolean enQueue(int value) {
        // First check the availability to accept a new node.
        if (this.count == this.capacity) {
            return false;
        }
        Node newNode = new Node(value);
        // Initialize the linked list
        if (this.count == 0) {
            this.head = this.tail = newNode;
        } else {
            this.tail.next = newNode;
            this.tail = newNode;
        }
        this.count += 1;
        return true;
    }
    
    public boolean deQueue() {
        if (this.count == 0) {
            return false;
        }
        if (this.count == 1) {
            this.head = this.tail = null;
        } else {
            this.head = this.head.next;
        }
        this.count -= 1;
        return true;
    }
    
    public int Front() {
        if (this.count == 0) {
            return -1;
        }
        return this.head.value;
    }
    
    public int Rear() {
        if (this.count == 0) {
            return -1;
        }
        return this.tail.value;
    }
    
    public boolean isEmpty() {
        return this.count == 0;
    }
    
    public boolean isFull() {
        return this.count == this.capacity;
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */