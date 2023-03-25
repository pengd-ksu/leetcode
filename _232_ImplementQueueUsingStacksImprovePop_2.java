class MyQueue {
    // old on top of stack1, new on top of stack2
    private Stack<Integer> stack1;
    private Stack<Integer> stack2;
    private int front;

    public MyQueue() {
        stack1 = new Stack<>();
        stack2 = new Stack<>();
    }
    
    public void push(int x) {
        if (stack1.isEmpty()) {
            front = x;
        }
        stack1.push(x);
    }
    
    public int pop() {
        if (stack2.isEmpty()) {
            while (!stack1.isEmpty()) {
                stack2.push(stack1.pop());
            }
        }
        return stack2.pop();
    }
    
    public int peek() {
        // stack2 if not empty, will contain all the older ele.
        // So need to check stack2 first. If stack2 is empty,
        // then the front in stack1 is the current peek ele.
        if (!stack2.isEmpty()) {
            return stack2.peek();
        }
        return front;
    }
    
    public boolean empty() {
        return (stack1.isEmpty()) && (stack2.isEmpty());
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */