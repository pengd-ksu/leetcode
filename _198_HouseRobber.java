class Solution {
    public int rob(int[] nums) {
        int N = nums.length;
        int[] memo = new int[N + 1];
        memo[0] = 0;
        memo[1] = nums[0];
        for (int i = 2; i < N + 1; i++) {
            memo[i] = Math.max(memo[i-1], memo[i-2] + nums[i-1]);
        }
        return memo[N];
    }
}