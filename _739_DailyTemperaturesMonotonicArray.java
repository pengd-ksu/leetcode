class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        int[] result = new int[n];
        int hottest = 0;

        for (int curr = n - 1; curr >= 0; curr--) {
            int currT = temperatures[curr];
            if (currT >= hottest) {
                hottest = currT;
                continue;
            }
            int inc = 1;
            while(temperatures[curr + inc] <= currT) {
                inc += result[curr + inc];
            }
            result[curr] = inc;
        }
        return result;
    }
}