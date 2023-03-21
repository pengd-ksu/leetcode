class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        int[] result = new int[n];// initialized values are 0s.
        for (int day = 0; day < n; day++) {
            for (int inc = 1; inc < n - day; inc++) {
                if (temperatures[day + inc] > temperatures[day]) {
                    result[day] = inc;
                    break;
                }
            }
        }
        return result;
    }
}