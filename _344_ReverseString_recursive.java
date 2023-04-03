class Solution {
    public void reverseString(char[] s) {
        int left = 0;
        int right = s.length - 1;
        helper(s, left, right);
    }
    public void helper(char[] s, int left, int right) {
        if (left >= right) {
            return;
        }
        char tmp = s[left];
        s[left] = s[right];
        s[right] = tmp;
        helper(s, left + 1, right - 1);
    }
}