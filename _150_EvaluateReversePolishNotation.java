class Solution {
    private HashSet<String> set;

    public Solution() {
        set = new HashSet<>(Arrays.asList("+", "-", "*", "/"));
    }

    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        for (String t : tokens) {
            if (!set.contains(t)) {
                stack.push(Integer.valueOf(t));
                continue;
            }
            int second = stack.pop();
            int first = stack.pop();
            int result = 0;
            switch(t) {
                case "+":
                    result = first + second;
                    break;
                case "-":
                    result = first - second;
                    break;
                case "*":
                    result = first * second;
                    break;
                case "/":
                    result = first / second;
                    break;
            }
            stack.push(result);
        }
        return stack.pop();
    }
}