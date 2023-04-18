class Solution {
    public int rob(int[] nums) {
        if (nums.length == 1) {
            return nums[0];
        }
        int robStartFirst = robMax(nums, 0, nums.length - 2);
        int robStartSecond = robMax(nums, 1, nums.length - 1);
        return Math.max(robStartFirst, robStartSecond);
    }

    // handle eles more than 2
    public int robMax(int[]nums, int start, int end) {
        // There are more than 3 eles in nums.
        int prev, curr;
        prev = 0;
        curr = 0;
        for (int i = start; i <= end; i++) {
            int tmp = curr;
            curr = Math.max(prev + nums[i], curr);
            prev = tmp;
        }
        return Math.max(curr, prev);
    }
}