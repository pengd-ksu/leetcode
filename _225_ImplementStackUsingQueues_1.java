class MyStack {
    private Queue<Integer> q1;
    private Queue<Integer> q2;
    private int first;

    public MyStack() {
        q1 = new LinkedList<>();
        q2 = new LinkedList<>();
    }
    
    public void push(int x) {
        first = x;
        q1.add(x);
    }
    
    public int pop() {
        while (q1.size() > 1) {
            first = q1.remove();
            q2.add(first);
        }
        int res = q1.remove();
        q1 = q2;
        q2 = new LinkedList<>(); 
        return res;
    }
    
    public int top() {
        return first;
    }
    
    public boolean empty() {
        return q1.isEmpty();
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */