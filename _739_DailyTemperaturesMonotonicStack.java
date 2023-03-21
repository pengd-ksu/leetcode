class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        int[] result = new int[n];
        Stack<Integer> stack = new Stack<>();

        for (int day = 0; day < n; day++) {
            int curr = temperatures[day];
            while (!stack.isEmpty() && (temperatures[stack.peek()] < curr)) {
                int prev = stack.pop();
                result[prev] = day - prev;
            }
            stack.push(day);
        }
        // The rest on the stack has initialized values 0.
        return result;
    }
}