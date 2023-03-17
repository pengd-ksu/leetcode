class MovingAverage {
    private Queue<Integer> q;
    private int count, capacity;
    private double sum;
    
    public MovingAverage(int size) {
        this.q = new LinkedList<>();
        this.capacity = size;
    }
    
    public double next(int val) {
        if (this.count == this.capacity) {
            this.sum -= this.q.remove();
            this.q.add(val);
            this.sum += val;
            return sum / count;
        }
        this.q.add(val);
        this.count += 1;
        this.sum += val;
        return this.sum / this.count;
    }
}

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage obj = new MovingAverage(size);
 * double param_1 = obj.next(val);
 */