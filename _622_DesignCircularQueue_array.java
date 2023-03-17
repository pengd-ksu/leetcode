class MyCircularQueue {
    private int[] queue;
    private int head;
    private int capacity;
    private int count;

    public MyCircularQueue(int k) {
        this.queue = new int[k];
        this.head = 0;
        this.capacity = k;
        this.count = 0;
    }
    
    public boolean enQueue(int value) {
        if (this.count == this.capacity) {
            return false;
        }
        queue[(this.head + this.count)%capacity] = value;
        this.count += 1;
        return true;
    }
    
    public boolean deQueue() {
        if (this.count == 0) {
            return false;
        }
        this.head = (this.head + 1) % this.capacity;
        this.count -= 1;
        return true;
    }
    
    public int Front() {
        if (this.count == 0) {
            return -1;
        }
        return this.queue[this.head];
    }
    
    public int Rear() {
        if (this.count == 0) {
            return -1;
        }
        return this.queue[(this.head + this.count - 1) % this.capacity];
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