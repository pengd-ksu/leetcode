/*
Input: s = "3[a2[c]]"
Output: "accaccacc"
*/
class Solution {
    public String decodeString(String s) {
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == ']') {
                List<Character> decode = new ArrayList<>();
                while (stack.peek() != '[') {
                    decode.add(stack.pop());
                }
                stack.pop();// pop '['
                int base = 1;
                int num = 0;
                while (!stack.isEmpty() && Character.isDigit(stack.peek())) {
                    num = num + base * (stack.pop() - '0');
                    base *= 10;
                }
                while (num > 0) {
                    for (int j = decode.size() - 1; j >= 0; j--) {
                        stack.push(decode.get(j));;
                    }
                    num -= 1;
                }
            } else {
                stack.push(s.charAt(i));
            }
        }
        StringBuilder res = new StringBuilder();
        while (!stack.isEmpty()) {
            res.append(stack.pop());
        }
        res.reverse();
        return res.toString();
    }
}