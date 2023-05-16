class Solution {
    public int[] shuffle(int[] nums, int n) {
        // 2, 5, 1, 3, 4, 7
        // 0, 1, 2, 3, 4, 5
        // 2, 3, 5, 4, 1, 7
        // 0, 3, 1, 4, 2, 5
        int[] res = new int[nums.length];
        for (int i = 0; i < n; i++) {
            res[2 * i] = nums[i];
            res[2 * i + 1] = nums[i + n];
        }
        return res;
    }
}