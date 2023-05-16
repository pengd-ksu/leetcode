class Solution {
    public int[] runningSum(int[] nums) {
        int start = 0;
        int[] res = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            res[i] = start + nums[i];
            start = res[i];
        }
        return res;
    }
}