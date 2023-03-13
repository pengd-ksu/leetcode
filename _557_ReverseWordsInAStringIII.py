class Solution {
    public String reverseWords(String s) {
        StringBuilder result = new StringBuilder();
        StringBuilder tmp = new StringBuilder();
        for(int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == ' ') {
                if (tmp.length() != 0) {
                    result.append(tmp.reverse().toString());
                }
                result.append(s.charAt(i));
                tmp = new StringBuilder();
            } else {
                tmp.append(s.charAt(i));
            }
        }
        if (tmp.length() != 0) {
            result.append(tmp.reverse().toString());
        }
        return result.toString();
    }
}