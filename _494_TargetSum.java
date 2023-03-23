class Solution {
    private int dfs(int[] nums, int idx, int sum, int target) {
        if (idx == nums.length) {
            return(sum == target? 1 : 0);
        }
        return dfs(nums, idx+1, sum+nums[idx], target) 
                + dfs(nums, idx+1, sum-nums[idx], target);
    }

    public int findTargetSumWays(int[] nums, int target) {
        return dfs(nums, 0, 0, target);
    }
}