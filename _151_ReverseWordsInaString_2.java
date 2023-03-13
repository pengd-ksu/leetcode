class Solution {
    public String reverseWords(String s) {
        String[] words = s.trim().split(" ", -1);
        StringBuilder res = new StringBuilder();
        for (int i = words.length-1; i >= 0; i--) {
            // split usually brings " "
            if (!words[i].isEmpty()) {
                res.append(words[i]).append(" ");
            }
        }
        return res.toString().trim();
    }
}