class MinStack {
    // In this solution, we store a pair of values on the stack,
    // the first ele is the val, and the second ele is current min.
    // There might be some repetitives, since a min might correspond
    // to a consecutive of eles.
    private Stack<int[]> stack;

    public MinStack() {
        stack = new Stack<>();
    }
    
    public void push(int val) {
        if (stack.isEmpty()) {
            stack.push(new int[] {val, val});
        } else {
            int newMin = Math.min(val, stack.peek()[1]);
            stack.push(new int[] {val, newMin});
        }
    }
    
    public void pop() {
        stack.pop();
    }
    
    public int top() {
        return stack.peek()[0];
    }
    
    public int getMin() {
        return stack.peek()[1];
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */