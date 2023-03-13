class Solution {
    public void moveZeroes(int[] nums) {
        if (nums.length <= 1) return;
        int i = 0, nz = 0;
        while (i < nums.length) {
            if (nums[i] != 0) {
                nums[nz] = nums[i];
                nz++;
            }
            i++;
        }
        while (nz < nums.length) {
            nums[nz] = 0;
            nz++;
        }
    }
}