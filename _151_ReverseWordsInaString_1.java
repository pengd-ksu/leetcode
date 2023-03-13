class Solution {
    public String reverseWords(String s) {
        s = s.trim();
        // split("\\s+") will split the string into string of array with separator as space or multiple spaces. \s+ is a regular expression for one or more spaces.
        List<String> wordList = Arrays.asList(s.split("\\s+"));
        Collections.reverse(wordList);
        return String.join(" ", wordList);
    }
}