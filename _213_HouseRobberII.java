class Solution {
    public int rob(int[] nums) {
        int N = nums.length;
        if (N < 2) {
            return nums[N-1];
        }
        // rob the first house, will not rob the last, only count
        // from 0 to N-2;
        int[] r1 = new int[N-1];
        r1[0] = nums[0];
        if (N > 2) {
            r1[1] = nums[0];
        }
        // not rob the first house, count all the way to N-1;
        int[] r2 = new int[N];
        r2[0] = 0;
        r2[1] = nums[1];
        for (int i = 2; i < N; i++) {
            if (i < N - 1) {
                r1[i] = Math.max(r1[i-2] + nums[i], r1[i-1]);
            }
            r2[i] = Math.max(r2[i-2] + nums[i], r2[i-1]);
        }
        return Math.max(r1[N-2], r2[N-1]);
    }
}