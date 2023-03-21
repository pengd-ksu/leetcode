class Solution {
    private HashMap<Character, Character> mp;

    public Solution() {
        mp = new HashMap<>();
        mp.put('{', '}');
        mp.put('[', ']');
        mp.put('(', ')');
    }

    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (mp.containsKey(c)) {
                stack.push(c);
            } else if (stack.isEmpty() || (!(mp.get(stack.pop()).equals(c)))) {
                return false;
            }
        }
        return stack.isEmpty();
    }
}